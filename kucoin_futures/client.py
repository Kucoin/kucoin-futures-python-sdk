from kucoin_futures.market.market_api import MarketApi
from kucoin_futures.trade.trade_api import TradeApi
from kucoin_futures.user.user import UserData
from kucoin_futures.ws_token.token import GetToken

# -- Reserved for former habitual users --
Market = MarketApi
User = UserData
Trade = TradeApi
WsToken = GetToken
# -- --


class FuturesApi(MarketApi, TradeApi):
    """
    All APIs for futures
    """
