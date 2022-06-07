#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import unittest
import sys
import os
import json


class TestUserApi(unittest.TestCase):

    def setUp(self) -> None:
        current_path = os.path.abspath(os.path.dirname(__file__))
        root = os.path.abspath(
            os.path.dirname(current_path) + os.path.sep + ".")

        sys.path.append(root)
        from kucoin_futures.client import FuturesApi
        from examples_config import gloabl_examples_api_config
        self.client = FuturesApi(**gloabl_examples_api_config)

    def json_print(self, ret):
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_get_active_contracts(self):
        ret = self.client.get_active_contracts()
        self.json_print(ret)

    def test_get_a_certain_contract(self):
        ret = self.client.get_a_certain_contract(symbol='BTCUSDTM')
        self.json_print(ret)


class TestUserApi(unittest.TestCase):

    pass

    # def get_risk_limit(self, symbol: str):
    #     self._filter_request(GET,
    #                          f"/api/v2/contracts/risk-limit/{symbol}",
    #                          auth=False)

    # def query_funding_history(
    #     self,
    #     symbol: str,
    #     startAt: Optional[int] = None,
    #     endAt: Optional[int] = None,
    #     limit: Optional[int] = None,
    #     fromId: Optional[int] = None,
    #     **kwargs,
    # ):
    #     params = {
    #         "symbol": symbol,
    #         "startAt": startAt,
    #         "endAt": endAt,
    #         "limit": limit,
    #         "fromId": fromId,
    #         **kwargs,
    #     }
    #     self._filter_request(GET,
    #                          f"/api/v2/funding-history",
    #                          params=params,
    #                          auth=False)

    # def get_klines(
    #     self,
    #     granularity: int,
    #     symbol: str,
    #     fro: Optional[int] = None,
    #     to: Optional[int] = None,
    #     **kwargs,
    # ):
    #     params = {
    #         "granularity": granularity,
    #         "symbol": symbol,
    #         "from": fro,
    #         "to": to,
    #         **kwargs,
    #     }
    #     self._filter_request(GET,
    #                          f"/api/v2/kline/query",
    #                          params=params,
    #                          auth=False)

    # def query_funding_rate_list(
    #     self,
    #     symbol: str,
    #     startAt: Optional[int] = None,
    #     endAt: Optional[int] = None,
    #     offset: Optional[int] = None,
    #     limit: Optional[int] = 50,
    #     **kwargs,
    # ):
    #     params = {
    #         "symbol": symbol,
    #         "startAt": startAt,
    #         "endAt": endAt,
    #         "offset": offset,
    #         "limit": limit,
    #         **kwargs,
    #     }
    #     self._filter_request(GET,
    #                          f"/api/v2/contract/{symbol}/funding-rates",
    #                          params=params,
    #                          auth=False)

    # def get_contract_mark_price(self, symbol: str):
    #     self._filter_request(GET,
    #                          f"/api/v2/mark-price/{symbol}/current",
    #                          auth=False)
