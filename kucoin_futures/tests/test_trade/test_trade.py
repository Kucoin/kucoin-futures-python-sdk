from kucoin_futures.tests.config import api_key, secret, passphrase
from kucoin_futures.trade.trade import TradeData


def test_get_max_open_size():
    trade = TradeData(key=api_key, secret=secret, passphrase=passphrase)

    print(trade.get_max_open_size(symbol="PEPEUSDTM", price="0.0000000001", leverage="10"))


def test_place_st_order():
    trade = TradeData(key=api_key, secret=secret, passphrase=passphrase)

    print(trade.place_st_order(symbol="XBTUSDM", side="buy", leverage="20", price="8000", size=1,
                               stopPriceType="TP", marginMode="ISOLATED", triggerStopUpPrice="9000",
                               triggerStopDownPrice="8000", timeInForce="GTC", type="limit"))