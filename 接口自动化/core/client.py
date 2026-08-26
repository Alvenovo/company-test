# -*- coding: utf-8 -*-
import requests

from config import HOSTS


class ApiClient:
    def __init__(self, side, token=""):
        self.side = side
        self.base = HOSTS[side].rstrip("/")
        self.session = requests.Session()
        self.session.headers["Content-Type"] = "application/json"
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"

    def post(self, path, body=None, timeout=30):
        resp = self.session.post(self.base + path, json=body or {}, timeout=timeout)
        return _wrap(resp)

    def get(self, path, params=None, timeout=30):
        resp = self.session.get(self.base + path, params=params, timeout=timeout)
        return _wrap(resp)


def _wrap(resp):
    try:
        body = resp.json()
    except Exception:
        body = {"_raw": resp.text[:500]}
    return {
        "http": resp.status_code,
        "state": body.get("state") if isinstance(body, dict) else None,
        "msg": body.get("msg") if isinstance(body, dict) else None,
        "body": body,
    }


def pick_list(result):
    data = (result.get("body") or {}).get("data") or {}
    if isinstance(data, dict) and isinstance(data.get("list"), list):
        return data["list"], data.get("pagination") or {}
    return [], {}
