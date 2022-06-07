#!/usr/bin/python
# -*- coding:utf-8 -*-
from typing import Optional
from kucoin_futures.base_request.base_request import KucoinFuturesBaseRestApi
from kucoin_futures.config import GET, POST


class UserConfig(KucoinFuturesBaseRestApi):

    def modify_auto_deposit_margin_status(
        self,
        symbol: str,
        autoDeposit: bool,
        **kwargs,
    ):
        params = {
            "symbol": symbol,
            "autoDeposit": autoDeposit,
            **kwargs,
        }
        return self._filter_request(POST,
                                    f"/api/v2/user-config/change-auto-deposit",
                                    params=params,
                                    auth=True)

    def get_global_leverage(
        self,
        symbol: str,
        **kwargs,
    ):
        params = {
            "symbol": symbol,
            **kwargs,
        }
        return self._filter_request(GET,
                                    f"/api/v2/user-config/leverage",
                                    params=params,
                                    auth=True)

    def get_global_leverages(
        self,
        **kwargs,
    ):
        params = {
            **kwargs,
        }
        return self._filter_request(GET,
                                    f"/api/v2/user-config/leverages",
                                    params=params,
                                    auth=True)

    def modify_global_leverage(
        self,
        symbol: str,
        leverage: int,
        **kwargs,
    ):
        params = {
            "symbol": symbol,
            "leverage": leverage,
            **kwargs,
        }
        return self._filter_request(POST,
                                    f"/api/v2/user-config/adjust-leverage",
                                    params=params,
                                    auth=True)


class Account(KucoinFuturesBaseRestApi):

    def list_of_all_sub_accounts(
        self,
        **kwargs,
    ):
        params = {
            **kwargs,
        }
        return self._filter_request(GET,
                                    f"/api/v2/sub-accounts",
                                    params=params,
                                    auth=True)

    def get_account_overview(
        self,
        currency: Optional[str] = None,
        **kwargs,
    ):
        params = {
            "currency": currency,
            **kwargs,
        }
        return self._filter_request(GET,
                                    f"/api/v2/account-overview",
                                    params=params,
                                    auth=True)

    def query_fund_record(
        self,
        limit: Optional[int] = 100,
        currency: Optional[str] = None,
        typ: Optional[str] = None,
        startAt: Optional[int] = None,
        endAt: Optional[int] = None,
        **kwargs,
    ):
        params = {
            "limit": limit,
            "currency": currency,
            "type": typ,
            "startAt": startAt,
            "endAt": endAt,
            **kwargs,
        }
        return self._filter_request(GET,
                                    f"/api/v2/transaction-history",
                                    params=params,
                                    auth=True)


class Transfer(KucoinFuturesBaseRestApi):

    def sub_transfer(
        self,
        amount: float,
        currency: str,
        subUserId: str,
        direction: str,
        accountType: str,
        subAccountType: str,
        **kwargs,
    ):
        params = {
            "amount": amount,
            "currency": currency,
            "subUserId": subUserId,
            "direction": direction,
            "accountType": accountType,
            "subAccountType": subAccountType,
            **kwargs,
        }
        return self._filter_request(POST,
                                    f"/api/v2/sub-transfer",
                                    params=params,
                                    auth=True)

    def transfer_out(
        self,
        amount: float,
        currency: str,
        recAccountType: str,
        **kwargs,
    ):
        params = {
            "amount": amount,
            "currency": currency,
            "recAccountType": recAccountType,
            **kwargs,
        }
        return self._filter_request(POST,
                                    f"/api/v2/account/transfer-out",
                                    params=params,
                                    auth=True)

    def query_transfer_out_request_record(
        self,
        startAt: Optional[int] = None,
        endAt: Optional[int] = None,
        limit: Optional[int] = None,
        currency: Optional[str] = None,
        status: Optional[str] = None,
        **kwargs,
    ):
        params = {
            "startAt": startAt,
            "endAt": endAt,
            "limit": limit,
            "currency": currency,
            "status": status,
            **kwargs,
        }
        return self._filter_request(GET,
                                    f"/api/v2/transfer-list",
                                    params=params,
                                    auth=True)

    def transfer_in(
        self,
        amount: float,
        currency: str,
        payAccountType: str,
        **kwargs,
    ):
        params = {
            "amount": amount,
            "currency": currency,
            "payAccountType": payAccountType,
            **kwargs,
        }
        return self._filter_request(POST,
                                    f"/api/v2/transfer-in",
                                    params=params,
                                    auth=True)


class UserApi(UserConfig, Account, Transfer):
    pass
