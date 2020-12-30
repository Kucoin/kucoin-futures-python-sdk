from kucoin_futures.base_request.base_request import KucoinFuturesBaseRestApi


class GetToken(KucoinFuturesBaseRestApi):

    def get_ws_token(self, is_private=False):
        """
        https://docs.kumex.com/#apply-for-connection-token
        :param is_private private or public
        :return:
        """
        uri = '/api/v1/bullet-public'
        if is_private:
            uri = '/api/v1/bullet-private'

        return self._request('POST', uri, auth=is_private)



