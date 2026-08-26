import pytest

from core.cdp_token import cdp_up, read_token
from core.client import ApiClient


@pytest.fixture(scope="session")
def admin_token():
    if not cdp_up():
        pytest.skip("Chrome 调试端口 9222 未开")
    token = read_token("admin")
    if not token:
        pytest.skip("平台后台未登录或 token 过期")
    return token


@pytest.fixture(scope="session")
def seller_token():
    if not cdp_up():
        pytest.skip("Chrome 调试端口 9222 未开")
    token = read_token("seller")
    if not token:
        pytest.skip("商户后台未登录或 token 过期")
    return token


@pytest.fixture(scope="session")
def admin(admin_token):
    return ApiClient("admin", admin_token)


@pytest.fixture(scope="session")
def seller(seller_token):
    return ApiClient("seller", seller_token)
