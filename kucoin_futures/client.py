from kucoin_futures.marke_data.market_data import MarketData
from kucoin_futures.trade.trade import TradeData
from kucoin_futures.user.user import UserData
from kucoin_futures.ws_token.token import GetToken


class Market(MarketData):
    pass


class User(UserData):
    pass


class Trade(TradeData):
    pass


class WsToken(GetToken):
    pass


