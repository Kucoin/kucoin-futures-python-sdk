from kucoin_futures.tests.config import api_key, secret, passphrase
from kucoin_futures.client import User


def test_get_account_overview_all():
    user = User(key=api_key, secret=secret, passphrase=passphrase)
    # test default currency:XBT
    res = user.get_account_overview_all()
    assert res['summary']['currency'] == 'XBT'
    # test currency:USDT
    res = user.get_account_overview_all("USDT")
    assert res['summary']['currency'] == 'USDT'
