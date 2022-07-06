#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import requests
import hmac
import hashlib
import base64
import time
from uuid import uuid1
from urllib.parse import urljoin
from typing import Dict, Optional

try:
    import pkg_resources

    version = "v" + pkg_resources.get_distribution("kucoin-futures-python").version
except (ModuleNotFoundError, pkg_resources.DistributionNotFound):
    version = "v2.0.0"  # use the version directly


class KucoinFuturesBaseRestApi(object):
    def __init__(
        self,
        key: Optional[str] = "",
        secret: Optional[str] = "",
        passphrase: Optional[str] = "",
        is_sandbox: Optional[bool] = False,
        url: Optional[str] = "",
        is_v1api: Optional[bool] = False,
    ) -> None:
        """
        https://docs.kucoin.com/futures/new

        :param key: Api Token Id  (Mandatory)
        :type key: string
        :param secret: Api Secret  (Mandatory)
        :type secret: string
        :param passphrase: Api Passphrase used to create API  (Mandatory)
        :type passphrase: string
        :param is_sandbox: True sandbox , False  (optional)
        """
        if url:
            self.url = url
        else:
            if is_sandbox:
                self.url = "https://api-sandbox-futures.kucoin.com"
            else:
                self.url = "https://api-futures.kucoin.com"
        self.key = key
        self.secret = secret
        self.passphrase = passphrase
        self.is_v1api = is_v1api

    def _request(
        self,
        method: str,
        uri: str,
        timeout: int = 5,
        auth: bool = True,
        params: Optional[Dict] = None,
    ):
        uri_path = uri
        data_json = ""
        if method in ["GET", "DELETE"]:
            if params:
                strl = []
                for key in sorted(params):
                    strl.append("{}={}".format(key, params[key]))
                data_json += "&".join(strl)
                uri += "?" + data_json
                uri_path = uri
        else:
            if params:
                data_json = json.dumps(params)
                uri_path = uri + data_json

        headers = {}
        if auth:
            now_time = int(time.time()) * 1000
            str_to_sign = str(now_time) + method + uri_path
            sign = base64.b64encode(
                hmac.new(
                    self.secret.encode("utf-8"),
                    str_to_sign.encode("utf-8"),
                    hashlib.sha256,
                ).digest()
            )
            if self.is_v1api:  # Now API KEY is generally not v1
                headers = {
                    "KC-API-SIGN": sign,
                    "KC-API-TIMESTAMP": str(now_time),
                    "KC-API-KEY": self.key,
                    "KC-API-PASSPHRASE": self.passphrase,
                    "Content-Type": "application/json",
                }
            else:
                passphrase = base64.b64encode(
                    hmac.new(
                        self.secret.encode("utf-8"),
                        self.passphrase.encode("utf-8"),
                        hashlib.sha256,
                    ).digest()
                )
                headers = {
                    "KC-API-SIGN": sign,
                    "KC-API-TIMESTAMP": str(now_time),
                    "KC-API-KEY": self.key,
                    "KC-API-PASSPHRASE": passphrase,
                    "Content-Type": "application/json",
                    "KC-API-KEY-VERSION": "2",
                }
        headers["User-Agent"] = "kucoin-futures-python-sdk/" + version
        url = urljoin(self.url, uri)

        if method in ["GET", "DELETE"]:
            response_data = requests.request(
                method, url, headers=headers, timeout=timeout
            )
        else:
            response_data = requests.request(
                method, url, headers=headers, data=data_json, timeout=timeout
            )
        return self.check_response_data(response_data)

    def _filter_request(
        self,
        *args,
        params: Optional[Dict] = None,
        **kwargs,
    ):
        """It filters request parameters with empty value

        Args:
            params (Optional[Dict], optional): Request parameter with empty unfiltered value. Defaults to None.
        """
        if params:
            params = filter_params = dict(
                filter(lambda val: val[1] is not None, params.items())
            )
        return self._request(*args, **kwargs, params=params)

    @staticmethod
    def check_response_data(response_data: requests.Response):
        if response_data.status_code == 200:
            try:
                data = response_data.json()
            except ValueError:
                raise Exception(response_data.content)
            else:
                if data and data.get("code"):
                    if data.get("code") == "200000":
                        if data.get("data"):
                            return data["data"]
                        else:
                            return data
                    else:
                        raise Exception(
                            "{}-{}".format(
                                response_data.status_code, response_data.text
                            )
                        )
        else:
            raise Exception(
                "{}-{}".format(response_data.status_code, response_data.text)
            )

    @property
    def return_unique_id(self) -> str:
        return uuid1().hex
