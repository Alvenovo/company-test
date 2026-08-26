import pytest

from core.client import pick_list
from data import GOODS_ID, MISSING_GOODS_ID

LIST = "/v3/goods/admin/goodsLogs/list"


@pytest.mark.api
@pytest.mark.admin
@pytest.mark.parametrize(
    "case, body, expect_empty",
    [
        ("已知 spu 精确搜索", {"pageNum": 1, "pageSize": 20, "goodsId": GOODS_ID}, False),
        ("不存在的 spu", {"pageNum": 1, "pageSize": 20, "goodsId": MISSING_GOODS_ID}, True),
    ],
)
def test_goods_log_search_by_spu(admin, case, body, expect_empty):
    result = admin.post(LIST, body)
    assert result["state"] == 200, f"{case}: {result['msg']}"
    rows, _ = pick_list(result)
    if expect_empty:
        assert rows == [] or all(str(x.get("goodsId")) != MISSING_GOODS_ID for x in rows)
        return
    assert rows, f"{case}: 有数据才做正向断言"
    assert all(str(x.get("goodsId")) == str(body["goodsId"]) for x in rows), case
