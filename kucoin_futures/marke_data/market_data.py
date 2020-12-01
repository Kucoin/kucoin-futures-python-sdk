from kucoin_futures.base_request.base_request import KucoinFuturesBaseRestApi


class MarketData(KucoinFuturesBaseRestApi):

    def get_server_timestamp(self):
        """
        https://docs.kumex.com/#server-time

        get server timestamp
        :return: 1570609496404
        """
        return self._request('GET', '/api/v1/timestamp', auth=False)

    def get_interest_rate(self, symbol, startAt=None, endAt=None, reverse=True, offset=0, forward=True, maxCount=10):
        """
        https://docs.kumex.com/#get-interest-rate-list

        :param symbol: interest symbol (Mandatory)
        :type: str
        :param startAt: start time(milisecond) (optional)
        :type: int
        :param endAt:  end time(milisecond) (optional)
        :type: int
        :param reverse: is reverse? (optional)
        :type: bool
        :param offset:  Start offset. The unique attribute of the last returned result of the last request. The data of (optional)
        the first page will be returned by default
        :type: int
        :param forward: his parameter functions to judge whether the lookup is forward or not (optional)
        :type: bool
        :param maxCount:Max record count (optional)
        :type : int
        :return:
            {'dataList':
                [
                    {'symbol': '.XBTINT', 'granularity': 60000, 'timePoint': 1570611840000, 'value': 0.0003},
                    {'symbol': '.XBTINT', 'granularity': 60000, 'timePoint': 1570611780000, 'value': 0.0003},
                    {'symbol': '.XBTINT', 'granularity': 60000, 'timePoint': 1570611720000, 'value': 0.0003},
                    {'symbol': '.XBTINT', 'granularity': 60000, 'timePoint': 1570611660000, 'value': 0.0003},
                    {'symbol': '.XBTINT', 'granularity': 60000, 'timePoint': 1570611600000, 'value': 0.0003},
                     {'symbol': '.XBTINT', 'granularity': 60000, 'timePoint': 1570611540000, 'value': 0.0003},
                     {'symbol': '.XBTINT', 'granularity': 60000, 'timePoint': 1570611480000, 'value': 0.0003},
                      {'symbol': '.XBTINT', 'granularity': 60000, 'timePoint': 1570611420000, 'value': 0.0003},
                      {'symbol': '.XBTINT', 'granularity': 60000, 'timePoint': 1570611360000, 'value': 0.0003},
                      {'symbol': '.XBTINT', 'granularity': 60000, 'timePoint': 1570611300000, 'value': 0.0003}
                        ],
                    'hasMore': True}
        """

        params = {'symbol': symbol}

        if startAt:
            params['startAt'] = startAt
        if endAt:
            params['endAt'] = endAt
        if reverse:
            params['reverse'] = reverse
        if offset:
            params['offset'] = offset
        if forward:
            params['forward'] = forward
        if maxCount:
            params['maxCount'] = maxCount

        return self._request('GET', '/api/v1/interest/query', auth=False, params=params)

    def get_index_list(self, symbol, startAt=None, endAt=None, reverse=True, offset=0, forward=True, maxCount=10):
        """
        https://docs.kumex.com/#get-index-list

        :param symbol: interest symbol (Mandatory)
        :type: str
        :param startAt: start time(milisecond) (optional)
        :type: int
        :param endAt:  end time(milisecond) (optional)
        :type: int
        :param reverse: is reverse? (optional)
        :type: bool
        :param offset:  Start offset. The unique attribute of the last returned result of the last request. The data of (optional)
        the first page will be returned by default
        :type: int
        :param forward: his parameter functions to judge whether the lookup is forward or not (optional)
        :type: bool
        :param maxCount:Max record count (optional)
        :type : int
        :return:
            {'dataList':
                [
                    {'symbol': '.BXBT','decomposionList': [
                            {'price': 8214.62, 'weight': 0.05746732, 'exchange': 'gemini'},
                            {'price': 8212.4, 'weight': 0.1896515, 'exchange': 'kraken'},
                            {'price': 8206.35, 'weight': 0.43039379, 'exchange': 'coinbase'},
                            {'price': 8221.60243, 'weight': 0.03994456, 'exchange': 'liquid'},
                            {'price': 8211.981, 'weight': 0.02333998, 'exchange': 'bittrex'}, {
                            'price': 8206.47, 'weight': 0.25920285, 'exchange': 'bitstamp'}],
                            'granularity': 5000, 'timePoint': 1570612465000, 'value': 8208.74},
                    {'symbol': '.BXBT','decomposionList': [
                            {'price': 8214.62, 'weight': 0.05746732, 'exchange': 'gemini'},
                            {'price': 8212.4, 'weight': 0.1896515, 'exchange': 'kraken'},
                            {'price': 8208.98, 'weight': 0.43039379, 'exchange': 'coinbase'},
                            {'price': 8221.60243, 'weight': 0.03994456, 'exchange': 'liquid'},
                            {'price': 8211.981, 'weight': 0.02333998, 'exchange': 'bittrex'},
                            {'price': 8207.47, 'weight': 0.25920285, 'exchange': 'bitstamp'}],
                            'granularity': 5000, 'timePoint': 1570612460000, 'value': 8210.14},
                    {......
                ],
            'hasMore': True}
        """
        params = {'symbol': symbol}

        if startAt:
            params['startAt'] = startAt
        if endAt:
            params['endAt'] = endAt
        if reverse:
            params['reverse'] = reverse
        if offset:
            params['offset'] = offset
        if forward:
            params['forward'] = forward
        if maxCount:
            params['maxCount'] = maxCount

        return self._request('GET', '/api/v1/index/query', auth=False, params=params)

    def get_current_mark_price(self, symbol):
        """
        https://docs.kumex.com/#get-current-mark-price

        :param symbol:
        :type: str
        :return: {'symbol': 'XBTUSDM', 'indexPrice': 8194.22, 'granularity': 5000, 'timePoint': 1570613025000, 'value': 8194.49}
        """

        return self._request('GET', '/api/v1/mark-price/{symbol}/current'.format(symbol=symbol), auth=False)

    def get_premium_index(self, symbol, startAt=None, endAt=None, reverse=True, offset=0, forward=True, maxCount=10):
        """
        https://docs.kumex.com/#get-premium-index

        :param symbol: interest symbol (Mandatory)
        :type: str
        :param startAt: start time(milisecond) (optional)
        :type: int
        :param endAt:  end time(milisecond) (optional)
        :type: int
        :param reverse: is reverse? (optional)
        :type: bool
        :param offset:  Start offset. The unique attribute of the last returned result of the last request. The data of (optional)
        the first page will be returned by default
        :type: int
        :param forward: his parameter functions to judge whether the lookup is forward or not (optional)
        :type: bool
        :param maxCount:Max record count (optional)
        :type : int
        :return:
         {
            "dataList": [
                      {
                        "symbol": ".XBTUSDMPI",              //Premium index symbol
                        "granularity": 60000,                //Granularity (milisecond)
                        "timePoint": 1558000320000,          //Time point (milisecond)
                        "value": 0.022585                    //Premium index
                      },
                      {
                        "symbol": ".XBTUSDMPI",
                        "granularity": 60000,
                        "timePoint": 1558000260000,
                        "value": 0.022611
                      },
                    ......
                ],
            "hasMore": true                        //Whether there are more pages
        }
        """

        params = {'symbol': symbol}

        if startAt:
            params['startAt'] = startAt
        if endAt:
            params['endAt'] = endAt
        if reverse:
            params['reverse'] = reverse
        if offset:
            params['offset'] = offset
        if forward:
            params['forward'] = forward
        if maxCount:
            params['maxCount'] = maxCount

        return self._request('GET', '/api/v1/premium/query', auth=False, params=params)

    def get_current_fund_rate(self, symbol):
        """
        https://docs.kumex.com/#get-current-funding-rate

        :param symbol:  type str (Mandatory)
        :return:
          {
                "symbol": ".XBTUSDMFPI8H",              //Funding Rate Symbol
                "granularity": 28800000,               //Granularity (milisecond)
                "timePoint": 1558000800000,            //Time point (milisecond)
                "value": 0.00375,                      //Funding rate
                "predictedValue": 0.00375              //Predicted funding rate
            }

        """

        return self._request('GET', '/api/v1/funding-rate/{symbol}/current'.format(symbol=symbol), auth=False)

    def get_trade_history(self, symbol):
        """
        https://docs.kumex.com/#transaction-history

        :param symbol:  type str (Mandatory)
        :return:
            [{
            "sequence": 102,                            //Sequence number
            "tradeId": "5cbd7377a6ffab0c7ba98b26",      //Transaction ID
            "takerOrderId": "5cbd7377a6ffab0c7ba98b27", //Taker order ID
            "makerOrderId": "5cbd7377a6ffab0c7ba98b28", //Maker order ID
            "price": "7000.0",                          //Filled price
            "size": 0.1,                                //Filled quantity
            "side": "buy",                              //Side-taker
            "ts": 1545904567062140823                   //Filled time - nanosecond
        },
        .......]

        """
        params = {
            'symbol': symbol
        }

        return self._request('GET', '/api/v1/trade/history', auth=False, params=params)

    def l2_order_book(self, symbol):
        """
        https://docs.kumex.com/#get-full-order-book-level-2

        :param symbol: type tar (Mandatory)
        :return:
        {
              "symbol": "XBTUSDM",      //Symbol
              "sequence": 100,          //Ticker sequence number
              "asks": [
                ["5000.0", 1000],       //Price, quantity
                ["6000.0", 1983],       //Price, quantity
                ......
              ],
              "bids": [
                ["3200.0", 800],        //Price, quantity
                ["3100.0", 100],        //Price, quantity
                ......
              ]
            }
        """

        params = {
            "symbol": symbol
        }
        return self._request('GET', '/api/v1/level2/snapshot', auth=False, params=params)

    def l2_part_order_book(self, symbol, depth=20):
        """
        https://docs.kucoin.com/futures/#get-part-order-book-level-2
        :param symbol: type tar (Mandatory)
        :return:
            {
            "code": "200000",
            "data": {
              "symbol": "XBTUSDM",      //Symbol
              "sequence": 100,          //Ticker sequence number
              "asks": [
                ["5000.0", 1000],   //Price, quantity
                ["6000.0", 1983]        //Price, quantity
              ],
              "bids": [
                ["3200.0", 800],        //Price, quantity
                ["3100.0", 100]     //Price, quantity
              ]
            }
            }
        """

        params = {
            "symbol": symbol
        }
        return self._request('GET', f'/api/v1/level2/depth{depth}', auth=False, params=params)

    def get_l2_messages(self, symbol, start, end):
        """

        :param symbol: type tar (Mandatory)
        :type: str
        :param start: Start sequence number (included in the returned data) (Mandatory)
        :type: int
        :param end:	End sequence number (included in the returned data) (Mandatory)
        :type: int
        :return:
        """
        params = {
            'symbol': symbol,
            'start': start,
            'end': end
        }

        return self._request('GET', '/api/v1/level2/message/query', auth=False, params=params)

    def l3_order_book(self, symbol):
        """
        https://docs.kumex.com/#get-full-order-book-level-3

        :param symbol: type tar (Mandatory)
        :return:
          {
            "code": "200000",
            "data": {
                "symbol": "XBTUSDM",        //Symbol
              "sequence":  100,     //The sequence number of the last received message in building a Level 3 order book
              "bids": [[5567483701231, "dfa123124", "123.12312", 10, 5567483701231], ...],  //Selling data: order placing time - nanosecond, order ID, price, quantity, time at which the order enters the order book -  nanosecond
              "asks": [[5567483701231, "dfa123124", "123.12312", 10, 5567483701231], ...]   //Buying data: order placing time - nanosecond, order ID, price, quantity, time at which the order enters the order book- nanosecond
            }
          }
        """

        params = {
            "symbol": symbol
        }
        return self._request('GET', '/api/v1/level3/snapshot', auth=False, params=params)

    def l3_order_book_v2(self, symbol):
        """
        https://docs.kucoin.com/futures/#get-full-order-book-level-3-v2
        :param symbol: type tar (Mandatory)
        :return:
          {
            "code": "200000",
            "data": {
                "symbol": "XBTUSDM",        //Symbol
              "sequence":  100,     //The sequence number of the last received message in building a Level 3 order book
              "bids": [[5567483701231, "dfa123124", "123.12312", 10, 5567483701231], ...],  //Selling data: order placing time - nanosecond, order ID, price, quantity, time at which the order enters the order book -  nanosecond
              "asks": [[5567483701231, "dfa123124", "123.12312", 10, 5567483701231], ...]   //Buying data: order placing time - nanosecond, order ID, price, quantity, time at which the order enters the order book- nanosecond
            }
          }
        """

        params = {
            "symbol": symbol
        }
        return self._request('GET', '/api/v2/level3/snapshot', auth=False, params=params)

    def get_l3_messages(self, symbol, start, end):
        """

        :param symbol: type tar (Mandatory)
        :type: str
        :param start: Start sequence number (included in the returned data) (Mandatory)
        :type: int
        :param end:	End sequence number (included in the returned data) (Mandatory)
        :type: int
        :return:
         [
        {
          "symbol": "XBTUSDM",          //Symbol
          "sequence": 1,                //Message sequence number
          "side": "sell",               //Order side
          "orderTime": 1558074650840002300,       //Order placing time
          "size": 10,                   //Order quantity
          "orderId": "5cde551aa14a9cad7e454374", //Order ID
          "price": "7000.0",            //Order price
          "type": "open",                             //Message type
          "clientOid": "xxxxxxxxxx",                  //Optional, this is a user-defined parameter which is used to identify the order
          "ts": 1558074652423004000               //Time at which the order enters the order book- nanosecond
        },
        {
          "symbol": "XBTUSDM",          //Symbol
          "reason": "canceled",     //Reason: canceld or filled
          "sequence": 2,                //Message sequence number
          "orderId": "5cde551aa14a9cad7e454374", //Order ID
          "type": "done",               //Message type
          "ts": 1558075303543002400 //Time at which the order is removed- nanosecond
        }
    ]
        """
        params = {
            'symbol': symbol,
            'start': start,
            'end': end
        }

        return self._request('GET', '/api/v1/level3/message/query', auth=False, params=params)

    def get_ticker(self, symbol):
        """
        https://docs.kumex.com/#get-real-time-ticker
        :param symbol: type tar (Mandatory)
        :return:
        {
          "sequence": 1001,             //Sequence number
          "symbol": "XBTUSDM",              //Symbol
          "side": "buy",                    //Side of liquidity taker
          "size": 10,                       //Filled quantity
          "price": "7000.0",                //Filled price
          "bestBidSize": 20,                //Best bid size
          "bestBidPrice": "7000.0",     //Best bid
          "bestAskSize": 30,                //Best ask size
          "bestAskPrice": "7001.0",     //Best ask
          "tradeId": "5cbd7377a6ffab0c7ba98b26",  //Transaction ID
          "ts": 1550653727731              //Filled time - nanosecond
        }
        """
        params = {
            'symbol': symbol
        }

        return self._request('GET', '/api/v1/ticker', auth=False, params=params)

    def get_contracts_list(self):
        """
        :return:
        {
          "baseCurrency": "XBT",  //Base currency
          "fairMethod": "FundingRate", //Fair price marking method
          "fundingBaseSymbol": ".XBTINT8H",  //Ticker symbol of the based currency
          "fundingQuoteSymbol": ".USDINT8H", //Ticker symbol of the quote currency
          "fundingRateSymbol": ".XBTUSDMFPI8H",  //Funding rate symbol
          "indexSymbol": ".BXBT",    //Index symbol
          "initialMargin": 0.01, //Initial margin requirement
          "isDeleverage": true,   //Enabled ADL or not
          "isInverse": true,  //Reverse contract or not
          "isQuanto": false,   //Whether quanto or not
          "lotSize": 1,   //Minimum lot size
          "maintainMargin": 0.005,    //Maintenance margin requirement
          "makerFeeRate": -0.00025,  //Maker fees
          "makerFixFee": -0.0000000200,   //Fixed maker fees
          "markMethod": "FairPrice", //Marking method
          "maxOrderQty": 1000000,   //Maximum order quantity
          "maxPrice": 1000000.0000000000,  //Maximum order price
          "maxRiskLimit": 200,  //Maximum risk limit (unit: XBT)
          "minRiskLimit": 200,  //Minimum risk limit (unit: XBT)
          "multiplier": -1,    //Contract multiplier
          "quoteCurrency": "USD",  //Quote currency
          "riskStep": 100,  //Risk limit increment value (unit: XBT)
          "rootSymbol": "XBT", //Contract group
          "status": "Open", //Contract status
          "symbol": "XBTUSDM", //Ticker symbol of the contract
          "takerFeeRate": 0.0005,  //Taker fees
          "takerFixFee": 0.0000000600,   //Fixed taker fees
          "tickSize": 1,  //Minimum price changes
          "type": "FFWCSX"    //Type of the contract
        }
        """
        return self._request('GET', '/api/v1/contracts/active', auth=False)

    def get_contract_detail(self, symbol):
        """
        https://docs.kumex.com/#get-order-info-of-the-contract

        :param symbol: type tar (Mandatory)
        :return:
        {
          "baseCurrency": "XBT",  //Base currency
          "fairMethod": "FundingRate", //Fair price marking method
          "fundingBaseSymbol": ".XBTINT8H",  //Ticker symbol of the based currency
          "fundingQuoteSymbol": ".USDINT8H", //Ticker symbol of the quote currency
          "fundingRateSymbol": ".XBTUSDMFPI8H",  //Funding rate symbol
          "indexSymbol": ".BXBT",    //Index symbol
          "initialMargin": 0.01, //Initial margin requirement
          "isDeleverage": true,   //Enabled ADL or not
          "isInverse": true,  //Reverse contract or not
          "isQuanto": false,   //Whether quanto or not
          "lotSize": 1,   //Minimum lot size
          "maintainMargin": 0.005,    //Maintenance margin requirement
          "makerFeeRate": -0.00025,  //Maker fees
          "makerFixFee": -0.0000000200,   //Fixed maker fees
          "markMethod": "FairPrice", //Marking method
          "maxOrderQty": 1000000,   //Maximum order quantity
          "maxPrice": 1000000.0000000000,  //Maximum order price
          "maxRiskLimit": 200,  //Maximum risk limit (unit: XBT)
          "minRiskLimit": 200,  //Minimum risk limit (unit: XBT)
          "multiplier": -1,    //Contract multiplier
          "quoteCurrency": "USD",  //Quote currency
          "riskStep": 100,  //Risk limit increment value (unit: XBT)
          "rootSymbol": "XBT", //Contract group
          "status": "Open", //Contract status
          "symbol": "XBTUSDM", //Ticker symbol of the contract
          "takerFeeRate": 0.0005,  //Taker fees
          "takerFixFee": 0.0000000600,   //Fixed taker fees
          "tickSize": 1,  //Minimum price changes
          "type": "FFWCSX"    //Type of the contract
        }
        """
        return self._request('GET', '/api/v1/contracts/{symbol}'.format(symbol=symbol), auth=False)

    def get_kline_data(self, symbol, granularity:int, begin_t=None, end_t=None):
        """
        https://docs.kucoin.com/futures/#get-k-line-data-of-contract
        :param symbol: type tar (Mandatory)
        :return:
            [
            1575331200000,//时间
            7495.01,      //开盘价
            8309.67,      //最高价
            7250,         //最低价
            7463.55,      //收盘价
            0             //成交量
        ],
        [
            1575374400000,
            7464.37,
            8297.85,
            7273.02,
            7491.44,
            0
        ]
        """
        params = {
            "symbol": symbol,
            "granularity": granularity
        }
        if begin_t:
            params.update({"from": begin_t})
        if end_t:
            params.update({"to": end_t})

        return self._request('GET', '/api/v1/kline/query', auth=False, params=params)

    def get_service_status(self):
        """
        https://docs.kucoin.com/futures/#get-the-service-status
        :param symbol: type tar (Mandatory)
        :return:
        {
        "status": "open",                //open, close, cancelonly
        "msg":  "upgrade match engine"   //remark for operation
        }
        """
        return self._request('GET', '/api/v1/status', auth=False)

