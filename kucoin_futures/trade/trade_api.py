#!/usr/bin/python
# -*- coding:utf-8 -*-
from typing import Optional
from kucoin_futures.base_request.base_request import KucoinFuturesBaseRestApi
from kucoin_futures.config import GET, POST, DELETE


class Order(KucoinFuturesBaseRestApi):
    def order_placement(
        self,
        symbol: str,
        side: str,
        typ: str,
        price: Optional[float] = None,
        size: Optional[int] = None,
        clientOid: Optional[str] = None,
        reduceOnly: Optional[bool] = False,
        closeOrder: Optional[bool] = False,
        hidden: Optional[bool] = None,
        visibleSize: Optional[int] = None,
        stopPrice: Optional[float] = None,
        postOnly: Optional[bool] = None,
        workingType: Optional[str] = None,
        timeInForce: Optional[str] = None,
        clientTimestamp: Optional[int] = None,
        allowMaxTimeWindow: Optional[int] = None,
        **kwargs,
    ):
        params = {
            "symbol": symbol,
            "side": side,
            "type": typ,
            "price": price,
            "size": size,
            "clientOid": clientOid,
            "reduceOnly": reduceOnly,
            "closeOrder": closeOrder,
            "hidden": hidden,
            "visibleSize": visibleSize,
            "stopPrice": stopPrice,
            "postOnly": postOnly,
            "workingType": workingType,
            "timeInForce": timeInForce,
            "clientTimestamp": clientTimestamp,
            "allowMaxTimeWindow": allowMaxTimeWindow,
            **kwargs,
        }
        return self._filter_request(POST, f"/api/v2/order", params=params, auth=True)

    def single_order_cancellation(
        self,
        symbol: str,
        orderId: Optional[str] = None,
        clientOid: Optional[str] = None,
        **kwargs,
    ):
        params = {
            "symbol": symbol,
            "orderId": orderId,
            "clientOid": clientOid,
            **kwargs,
        }
        return self._filter_request(DELETE, f"/api/v2/order", params=params, auth=True)

    def batch_order_cancellation(self, symbol: str, **kwargs):
        params = {
            "symbol": symbol,
            **kwargs,
        }
        return self._filter_request(DELETE, f"/api/v2/orders", params=params, auth=True)

    def query_transaction_records(
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
            GET, f"/api/v2/orders/historical-trades", params=params, auth=True
        )

    def query_individual_orders_details(
        self,
        orderId: Optional[str] = None,
        clientOid: Optional[str] = None,
        **kwargs,
    ):
        params = {
            "orderId": orderId,
            "clientOid": clientOid,
            **kwargs,
        }
        return self._filter_request(
            GET, f"/api/v2/order/detail", params=params, auth=True
        )

    def query_active_orders(
        self,
        symbol: str,
        **kwargs,
    ):
        params = {
            "symbol": symbol,
            **kwargs,
        }
        return self._filter_request(
            GET, f"/api/v2/orders/active", params=params, auth=True
        )

    def query_all_active_orders(self, **kwargs):
        params = {
            **kwargs,
        }
        return self._filter_request(
            GET, f"/api/v2/orders/all-active", params=params, auth=True
        )

    def query_historical_orders(
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
            GET, f"/api/v2/orders/historical-trades", params=params, auth=True
        )


class Position(KucoinFuturesBaseRestApi):
    def get_the_position(
        self,
        symbol: str,
        **kwargs,
    ):
        params = {
            "symbol": symbol,
            **kwargs,
        }
        return self._filter_request(
            GET, f"/api/v2/symbol-position", params=params, auth=True
        )

    def get_all_position(self, **kwargs):
        params = {
            **kwargs,
        }
        return self._filter_request(
            GET, f"/api/v2/all-position", params=params, auth=True
        )

    def increase_position_margin(
        self,
        symbol: str,
        positionSide: str,
        amount: float,
        **kwargs,
    ):
        params = {
            "symbol": symbol,
            "positionSide": positionSide,
            "amount": amount,
            **kwargs,
        }
        return self._filter_request(
            POST, f"/api/v2/change-margin", params=params, auth=True
        )

    def position_pnl_history(
        self,
        symbol: Optional[str] = None,
        typ: Optional[str] = None,
        settleCurrency: Optional[str] = None,
        startAt: Optional[str] = None,
        endAt: Optional[str] = None,
        limit: Optional[int] = 50,
        **kwargs,
    ):
        params = {
            "symbol": symbol,
            "type": typ,
            "settleCurrency": settleCurrency,
            "startAt": startAt,
            "endAt": endAt,
            "limit": limit,
            **kwargs,
        }
        return self._filter_request(
            GET, f"/api/v2/close-pnl-his", params=params, auth=True
        )


class TradeApi(Order, Position):
    pass
