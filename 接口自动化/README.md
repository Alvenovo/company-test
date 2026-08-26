# 华硕新商城接口自动化（个人备份）

pytest + requests。鉴权不写账号密码：复用本机 Chrome 调试端口里已经登录的后台 token。

```text
pip install -r requirements.txt
pytest -m smoke
pytest -k goods_log
```

没开浏览器或没登录时，需要 token 的用例会 skip，不当失败。`test_admin_without_token_asks_login` 不依赖登录。

## 结构

| 路径 | 干什么 |
|---|---|
| `tests/` | 新任务加 `test_*.py` |
| `core/cdp_token.py` | 从 CDP 读 token |
| `core/client.py` | 带 Authorization 调 `/v3` |
| `conftest.py` | session 级 admin / seller fixture |
| `config.py` | 环境地址，无密码 |

## 明确没有

Allure、Jenkins、Page Object、UI 自动化。面试不要说已经有这些。
