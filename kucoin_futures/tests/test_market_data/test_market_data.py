from kucoin_futures.marke_data.market_data import MarketData
from kucoin_futures.tests.config import api_key, secret, passphrase


def test_get_all_tickers():
    market = MarketData(key=api_key, secret=secret, passphrase=passphrase)
    for data in market.get_all_tickers():
        print(data)