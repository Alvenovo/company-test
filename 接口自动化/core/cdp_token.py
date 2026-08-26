# -*- coding: utf-8 -*-
"""从已登录的 Chrome（调试端口 9222）读取 token。不在本文件保存任何密钥。"""
import json
import time
import urllib.request

import websocket

from config import CDP, HOME, HOSTS

TOKEN_JS = """
(() => {
  const raw = localStorage.getItem("sld_token") || localStorage.getItem("access_token") || "";
  return String(raw).replace(/^"(.*)"$/, "$1");
})()
"""


def _pages():
    return json.load(urllib.request.urlopen(f"{CDP}/json/list", timeout=5))


def _find(host):
    for page in _pages():
        if page.get("type") == "page" and host in page.get("url", ""):
            return page
    return None


class _CDP:
    def __init__(self, page):
        self.ws = websocket.create_connection(
            page["webSocketDebuggerUrl"], timeout=30, suppress_origin=True
        )
        self.i = 0
        self.send("Runtime.enable")

    def send(self, method, params=None, timeout=20):
        self.i += 1
        self.ws.send(json.dumps({"id": self.i, "method": method, "params": params or {}}))
        end = time.time() + timeout
        while time.time() < end:
            data = json.loads(self.ws.recv())
            if data.get("id") == self.i:
                return data
        raise TimeoutError(method)

    def eval(self, expr):
        res = self.send(
            "Runtime.evaluate",
            {"expression": expr, "returnByValue": True, "awaitPromise": True},
        )
        return res.get("result", {}).get("result", {}).get("value")

    def goto(self, url):
        self.send("Page.enable")
        self.send("Page.navigate", {"url": url})
        time.sleep(2)

    def close(self):
        self.ws.close()


def read_token(side):
    host = HOSTS[side].replace("https://", "")
    page = _find(host)
    if not page:
        try:
            page = json.load(
                urllib.request.urlopen(
                    urllib.request.Request(f"{CDP}/json/new?{HOSTS[side]}{HOME[side]}", method="PUT"),
                    timeout=8,
                )
            )
            time.sleep(2)
        except Exception:
            return ""
    cdp = _CDP(page)
    try:
        href = cdp.eval("location.href") or ""
        if host not in href or "/login" in href:
            cdp.goto(f"{HOSTS[side]}{HOME[side]}")
        href = cdp.eval("location.href") or ""
        if "/login" in href:
            return ""
        return cdp.eval(TOKEN_JS) or ""
    except Exception:
        return ""
    finally:
        cdp.close()


def cdp_up():
    try:
        urllib.request.urlopen(f"{CDP}/json/version", timeout=3).read()
        return True
    except Exception:
        return False
