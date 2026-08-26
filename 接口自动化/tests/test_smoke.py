import pytest

from core.client import ApiClient, pick_list


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.admin
def test_admin_goods_log_list(admin):
    """已登录时，商品日志列表接口应返回业务成功。"""
    result = admin.post("/v3/goods/admin/goodsLogs/list", {"pageNum": 1, "pageSize": 5})
    assert result["http"] == 200
    assert result["state"] == 200, result["msg"]
    rows, _ = pick_list(result)
    assert isinstance(rows, list)


@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.admin
def test_admin_without_token_asks_login():
    """对照：不带头应提示登录。不依赖登录态。"""
    guest = ApiClient("admin", token="")
    result = guest.post("/v3/goods/admin/goodsLogs/list", {"pageNum": 1, "pageSize": 5})
    text = f"{result.get('msg') or ''} {result.get('body')}"
    assert result["state"] != 200 or "登录" in text
