#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import unittest
import sys
import os
import json


class TestContract(unittest.TestCase):
    def setUp(self) -> None:
        current_path = os.path.abspath(os.path.dirname(__file__))
        root = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")

        sys.path.append(root)
        from kucoin_futures.client import FuturesApi
        from examples_config import gloabl_examples_api_config

        self.client = FuturesApi(**gloabl_examples_api_config)

    def json_print(self, ret):
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_get_active_contracts(self):  # pass
        ret = self.client.get_active_contracts()
        self.json_print(ret)

    def test_get_a_certain_contract(self):  # pass
        ret = self.client.get_a_certain_contract(symbol="BTCUSDTM")
        self.json_print(ret)

    def test_get_risk_limit(self):#pass
        ret = self.client.get_risk_limit(symbol="BTCUSDTM")
        self.json_print(ret)

    def test_get_klines(self):  # pass
        ret = self.client.get_klines(granularity=5, symbol="BTCUSDTM")
        self.json_print(ret)

    def test_query_funding_rate_list(self):  # pass
        ret = self.client.query_funding_rate_list(symbol="BTCUSDTM")
        self.json_print(ret)

    def test_get_contract_mark_price(self):
        ret = self.client.get_contract_mark_price(symbol="BTCUSDTM")
        self.json_print(ret)


class TestOrderBook(unittest.TestCase):
    def setUp(self) -> None:
        current_path = os.path.abspath(os.path.dirname(__file__))
        root = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")

        sys.path.append(root)
        from kucoin_futures.client import FuturesApi
        from examples_config import gloabl_examples_api_config

        self.client = FuturesApi(**gloabl_examples_api_config)

    def json_print(self, ret):
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_get_order_book(self):
        ret = self.client.get_order_book(symbol="BTCUSDTM")
        self.json_print(ret)

    def test_best_maker(self):
        ret = self.client.best_maker(symbol="BTCUSDTM")
        self.json_print(ret)


class TestQuotesSnapshot(unittest.TestCase):
    def setUp(self) -> None:
        current_path = os.path.abspath(os.path.dirname(__file__))
        root = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")

        sys.path.append(root)
        from kucoin_futures.client import FuturesApi
        from examples_config import gloabl_examples_api_config

        self.client = FuturesApi(**gloabl_examples_api_config)

    def json_print(self, ret):
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_get_the_latest_transaction_price(self):
        ret = self.client.get_the_latest_transaction_price(symbol="BTCUSDTM")
        self.json_print(ret)

    def test_get_most_recent_record(self):
        ret = self.client.get_most_recent_record(symbol="BTCUSDTM")
        self.json_print(ret)


class TestDate(unittest.TestCase):
    def setUp(self) -> None:
        current_path = os.path.abspath(os.path.dirname(__file__))
        root = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")

        sys.path.append(root)
        from kucoin_futures.client import FuturesApi
        from examples_config import gloabl_examples_api_config

        self.client = FuturesApi(**gloabl_examples_api_config)

    def json_print(self, ret):
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_get_server_time(self):  # pass
        ret = self.client.get_server_time()
        self.json_print(ret)


class TestServerStatus(unittest.TestCase):
    def setUp(self) -> None:
        current_path = os.path.abspath(os.path.dirname(__file__))
        root = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")

        sys.path.append(root)
        from kucoin_futures.client import FuturesApi
        from examples_config import gloabl_examples_api_config

        self.client = FuturesApi(**gloabl_examples_api_config)

    def json_print(self, ret):
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_get_server_status(self):  # null
        ret = self.client.get_server_status()
        self.json_print(ret)
