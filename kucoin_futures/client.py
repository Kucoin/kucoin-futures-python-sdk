#!/usr/bin/python
# -*- coding:utf-8 -*-
from kucoin_futures.market.market_api import MarketApi
from kucoin_futures.trade.trade_api import TradeApi
from kucoin_futures.user.user_api import UserApi
from kucoin_futures.ws_token.token import GetToken

# -- Reserved for former habitual users --
Market = MarketApi
User = UserApi
Trade = TradeApi
WsToken = GetToken
# -- --


class FuturesApi(MarketApi, TradeApi, UserApi):
    """
    All APIs for futures
    """