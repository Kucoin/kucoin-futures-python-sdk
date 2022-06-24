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
        """Modify the user's auto deposit margin status.

        https://docs.kucoin.com/futures/new/#modify-the-user-39-s-auto-deposit-margin-status
        """
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
        """Get the user’s global leverage

        https://docs.kucoin.com/futures/new/#get-the-user-s-global-leverage
        """
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
        """Get user global leverage (all contracts)

        https://docs.kucoin.com/futures/new/#get-user-global-leverage-all-contracts
        """
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
        """Modify the user’s global leverage

        https://docs.kucoin.com/futures/new/#modify-the-user-s-global-leverage
        """
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
        """Get the list of all sub-accounts
        
        https://docs.kucoin.com/futures/new/#get-the-list-of-all-sub-accounts
        """
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
        """Get Account Overview

        https://docs.kucoin.com/futures/#get-account-overview
        """
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
        """Query Fund Record

        https://docs.kucoin.com/futures/new/#query-fund-record
        """
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
        """Transfer between Master user and Sub-user

        https://docs.kucoin.com/futures/new/#transfer
        """
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
        """Transfer out to KuCoin main/trading account

        https://docs.kucoin.com/futures/new/#transfer-out-to-kucoin-main-trading-account
        """
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
        """Query transfer out request record

        https://docs.kucoin.com/futures/new/#query-transfer-out-request-record
        """
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
        """Fund transfer into futures account

        https://docs.kucoin.com/futures/new/#fund-transfer-into-futures-account
        """
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
