#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import unittest
import sys
import os
import json
import time


class TestUserConfig(unittest.TestCase):

    def setUp(self) -> None:
        current_path = os.path.abspath(os.path.dirname(__file__))
        root = os.path.abspath(
            os.path.dirname(current_path) + os.path.sep + ".")
        sys.path.append(root)
        from kucoin_futures.client import FuturesApi
        from examples_config import gloabl_examples_api_config
        self.client = FuturesApi(**gloabl_examples_api_config)

    def test_modify_auto_deposit_margin_status(self):  #pass
        ret = self.client.modify_auto_deposit_margin_status('BTCUSDTM', True)
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_get_global_leverage(self):  #pass
        ret = self.client.get_global_leverage(symbol='BTCUSDTM')
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_get_global_leverages(self):  #pass
        ret = self.client.get_global_leverages()
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_modify_global_leverage(self):#pass
        ret = self.client.modify_global_leverage(symbol='BTCUSDTM',
                                                 leverage=10)
        print(json.dumps(ret, ensure_ascii=False, indent=2))


class TestAccount(unittest.TestCase):

    def setUp(self) -> None:
        current_path = os.path.abspath(os.path.dirname(__file__))
        root = os.path.abspath(
            os.path.dirname(current_path) + os.path.sep + ".")
        sys.path.append(root)
        from kucoin_futures.client import FuturesApi
        from examples_config import gloabl_examples_api_config
        self.client = FuturesApi(**gloabl_examples_api_config)

    def test_list_of_all_sub_accounts(self):
        #error {"code":"415000","msg":"not support at present."}
        ret = self.client.list_of_all_sub_accounts()
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_get_account_overview(self):  #pass
        ret = self.client.get_account_overview()
        print(json.dumps(ret, ensure_ascii=False, indent=2))
        time.sleep(1)
        ret = self.client.get_account_overview(currency='USDT')
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_query_fund_record(self):  #pass
        ret = self.client.query_fund_record()
        print(json.dumps(ret, ensure_ascii=False, indent=2))


class TestTransfer(unittest.TestCase):

    def setUp(self) -> None:
        current_path = os.path.abspath(os.path.dirname(__file__))
        root = os.path.abspath(
            os.path.dirname(current_path) + os.path.sep + ".")
        sys.path.append(root)
        from kucoin_futures.client import FuturesApi
        from examples_config import gloabl_examples_api_config
        self.client = FuturesApi(**gloabl_examples_api_config)

    def test_sub_transfer(self):
        #error {"code":"415000","msg":"not support at present."}
        ret = self.client.sub_transfer(amount=0.01,
                                       currency='USDT',
                                       subUserId="11111",
                                       direction="OUT",
                                       accountType="MAIN",
                                       subAccountType="MAIN")
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_transfer_out(self):
        #{"code":"230034","msg":"not support operation"}
        ret = self.client.transfer_out(amount=0.01,
                                       currency='USDT',
                                       recAccountType="TRADE")
        print(json.dumps(ret, ensure_ascii=False, indent=2))

    def test_query_transfer_out_request_record(self):  #No data
        ret = self.client.query_transfer_out_request_record()
        print(json.dumps(ret, ensure_ascii=False, indent=2))
    
    def test_transfer_in(self):
        #error {"code":"415000","msg":"not support at present."}
        ret = self.client.transfer_in(amount=0.001, currency='USDT', payAccountType="TRADE")
        print(json.dumps(ret, ensure_ascii=False, indent=2))
        