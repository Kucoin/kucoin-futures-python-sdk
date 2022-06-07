#!/usr/bin/python
# -*- coding:utf-8 -*-
from kucoin_futures.base_request.base_request import KucoinFuturesBaseRestApi
from typing import Optional, Dict, Any
from kucoin_futures.config import GET


class Contract(KucoinFuturesBaseRestApi):
    def get_active_contracts(self):
        return self._filter_request(GET, "/api/v2/contracts/active", auth=False)

    def get_a_certain_contract(self, symbol: str):
        return self._filter_request(GET, f"/api/v2/contracts/{symbol}", auth=False)

    def get_risk_limit(self, symbol: str):
        return self._filter_request(
            GET, f"/api/v2/contracts/risk-limit/{symbol}", auth=False
        )

    def query_funding_history(
        self,
        symbol: str,
        startAt: Optional[int] = None,
        endAt: Optional[int] = None,
        limit: Optional[int] = None,
        fromId: Optional[int] = None,
        **kwargs,
    ):
        params = {
            "symbol": symbol,
            "startAt": startAt,
            "endAt": endAt,
            "limit": limit,
            "fromId": fromId,
            **kwargs,
        }
        return self._filter_request(
            GET, f"/api/v2/funding-history", params=params, auth=False
        )

    def get_klines(
        self,
        granularity: int,
        symbol: str,
        fro: Optional[int] = None,
        to: Optional[int] = None,
        **kwargs,
    ):
        params = {
            "granularity": granularity,
            "symbol": symbol,
            "from": fro,
            "to": to,
            **kwargs,
        }
        return self._filter_request(
            GET, f"/api/v2/kline/query", params=params, auth=False
        )

    def query_funding_rate_list(
        self,
        symbol: str,
        startAt: Optional[int] = None,
        endAt: Optional[int] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = 50,
        **kwargs,
    ):
        params = {
            "symbol": symbol,
            "startAt": startAt,
            "endAt": endAt,
            "offset": offset,
            "limit": limit,
            **kwargs,
        }
        return self._filter_request(
            GET, f"/api/v2/contract/{symbol}/funding-rates", params=params, auth=False
        )

    def get_contract_mark_price(self, symbol: str):
        return self._filter_request(
            GET, f"/api/v2/mark-price/{symbol}/current", auth=False
        )


class OrderBook(KucoinFuturesBaseRestApi):
    def get_order_book(self, symbol: str, limit: Optional[int] = 500, **kwargs):
        params = {"symbol": symbol, "limit": limit, **kwargs}
        return self._filter_request(
            GET, f"/api/v2/order-book", params=params, auth=False
        )

    def best_maker(self, symbol: str, **kwargs):
        params = {"symbol": symbol, **kwargs}
        return self._filter_request(
            GET, f"/api/v2/order-book", params=params, auth=False
        )


class QuotesSnapshot(KucoinFuturesBaseRestApi):
    def get_the_latest_transaction_price(self, symbol: str, **kwargs):
        params = {"symbol": symbol, **kwargs}
        return self._filter_request(
            GET, f"/api/v2/ticker/price", params=params, auth=False
        )

    def get_most_recent_record(self, symbol: str, limit: Optional[int] = 20, **kwargs):
        params = {"symbol": symbol, "limit": limit, **kwargs}
        return self._filter_request(
            GET, f"/api/v2/ticker/price", params=params, auth=False
        )


class Date(KucoinFuturesBaseRestApi):
    def get_server_time(self):
        return self._filter_request(GET, f"/api/v1/timestamp", auth=False)


class ServerStatus(KucoinFuturesBaseRestApi):
    def get_server_status(self):
        self._filter_request(GET, f"/api/v1/status", auth=False)


class MarketApi(Contract, OrderBook, QuotesSnapshot):
    pass
