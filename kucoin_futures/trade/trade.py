from kucoin_futures.base_request.base_request import KucoinFuturesBaseRestApi


class TradeData(KucoinFuturesBaseRestApi):

    def get_fund_history(self, symbol, startAt=None, endAt=None, reverse=True, offset=0, forward=True, maxCount=10):
        """
        https://docs.kumex.com/#get-funding-history

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
                "id": 36275152660006,                //id
                "symbol": "XBTUSDTM",                  //Symbol
                "timePoint": 1557918000000,          //Time point (milisecond)
                "fundingRate": 0.000013,             //Funding rate
                "markPrice": 8058.27,                //Mark price
                "positionQty": 10,                   //Position size
                "positionCost": -0.001241,           //Position value at settlement period
                "funding": -0.00000464               //Settled funding fees. A positive number means that the user received the funding fee, and vice versa.
                "settleCurrency": "XBT"             //settlement currency
              },
              .......
            ],
            "hasMore": true                         //Whether there are more pages
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

        return self._request('GET', '/api/v1/funding-history', params=params)

    def get_position_details(self, symbol):
        """
        https://docs.kumex.com/#get-position-details

        :param symbol: interest symbol (Mandatory)
        :type: str
        :return:
        {
            "id": "5ce3cda60c19fc0d4e9ae7cd",                //Position ID
            "symbol": "XBTUSDTM",                              //Symbol
            "autoDeposit": true,                             //Auto deposit margin or not
            "maintMarginReq": 0.005,                         //Maintenance margin requirement
            "riskLimit": 200,                                //Risk limit
            "realLeverage": 1.06,                            //Leverage of the order
            "crossMode": false,                              //Cross mode or not
            "delevPercentage": 0.1,                          //ADL ranking percentile
            "openingTimestamp": 1558433191000,               //Open time
            "currentTimestamp": 1558507727807,               //Current timestamp
            "currentQty": -20,                               //Current position
            "currentCost": 0.00266375,                       //Current position value
            "currentComm": 0.00000271,                       //Current commission
            "unrealisedCost": 0.00266375,                    //Unrealised value
            "realisedGrossCost": 0,                          //Accumulated realised gross profit value
            "realisedCost": 0.00000271,                      //Current realised position value
            "isOpen": true,                                  //Opened position or not
            "markPrice": 7933.01,                            //Mark price
            "markValue": 0.00252111,                         //Mark value
            "posCost": 0.00266375,                           //Position value
            "posCross": 1.2e-7,                              //Manually added margin
            "posInit": 0.00266375,                           //Leverage margin
            "posComm": 0.00000392,                           //Bankruptcy cost
            "posLoss": 0,                                    //Funding fees paid out
            "posMargin": 0.00266779,                         //Position margin
            "posMaint": 0.00001724,                          //Maintenance margin
            "maintMargin": 0.00252516,                       //Position margin
            "realisedGrossPnl": 0,                           //Accumulated realised gross profit value
            "realisedPnl": -0.00000253,                      //Realised profit and loss
            "unrealisedPnl": -0.00014264,                    //Unrealised profit and loss
            "unrealisedPnlPcnt": -0.0535,                    //Profit-loss ratio of the position
            "unrealisedRoePcnt": -0.0535,                    //Rate of return on investment
            "avgEntryPrice": 7508.22,                        //Average entry price
            "liquidationPrice": 1000000,                     //Liquidation price
            "bankruptPrice": 1000000                         //Bankruptcy price
            "settleCurrency": "XBT"                          //Currency used to clear and settle the trades
        }
        """
        params = {
            'symbol': symbol
        }
        return self._request('GET', '/api/v1/position', params=params)

    def get_all_position(self):
        """
        https://docs.kumex.com/#get-position-list
        :return:
        [{
          "id": "5ce3cda60c19fc0d4e9ae7cd",                //Position ID
          "symbol": "XBTUSDTM",                              //Symbol
          "autoDeposit": true,                             //Auto deposit margin or not
          "maintMarginReq": 0.005,                         //Maintenance margin requirement
          "riskLimit": 200,                                //Risk limit
          "realLeverage": 1.06,                            //Leverage of the order
          "crossMode": false,                              //Cross mode or not
          "delevPercentage": 0.1,                          //ADL ranking percentile
          "openingTimestamp": 1558433191000,               //Open time
          "currentTimestamp": 1558507727807,               //Current timestamp
          "currentQty": -20,                               //Current position
          "currentCost": 0.00266375,                       //Current position value
          "currentComm": 0.00000271,                       //Current commission
          "unrealisedCost": 0.00266375,                    //Unrealised value
          "realisedGrossCost": 0,                          //Accumulated realised gross profit value
          "realisedCost": 0.00000271,                      //Current realised position value
          "isOpen": true,                                  //Opened position or not
          "markPrice": 7933.01,                            //Mark price
          "markValue": 0.00252111,                         //Mark value
          "posCost": 0.00266375,                           //Position value
          "posCross": 1.2e-7,                              //Manually added margin
          "posInit": 0.00266375,                           //Leverage margin
          "posComm": 0.00000392,                           //Bankruptcy cost
          "posLoss": 0,                                    //Funding fees paid out
          "posMargin": 0.00266779,                         //Position margin
          "posMaint": 0.00001724,                          //Maintenance margin
          "maintMargin": 0.00252516,                       //Position margin
          "realisedGrossPnl": 0,                           //Accumulated realised gross profit value
          "realisedPnl": -0.00000253,                      //Realised profit and loss
          "unrealisedPnl": -0.00014264,                    //Unrealised profit and loss
          "unrealisedPnlPcnt": -0.0535,                    //Profit-loss ratio of the position
          "unrealisedRoePcnt": -0.0535,                    //Rate of return on investment
          "avgEntryPrice": 7508.22,                        //Average entry price
          "liquidationPrice": 1000000,                     //Liquidation price
          "bankruptPrice": 1000000                         //Bankruptcy price
          "settleCurrency": "XBT"                         //Currency used to clear and settle the trades
        },
        ....]
        """
        return self._request('GET', '/api/v1/positions')

    def modify_auto_deposit_margin(self, symbol, status=True):
        """
        https://docs.kumex.com/#enable-disable-of-auto-deposit-margin

        :param  symbol: interest symbol (Mandatory)
        :param status: True is open, False is off  default True (Mandatory)
        :type: bool
        :return:  'True' or 'False'
        """
        params = {
            'symbol': symbol,
            'status': status
        }

        return self._request('POST', '/api/v1/position/margin/auto-deposit-status', params=params)

    def add_margin_manually(self, symbol, margin, bizNo):
        """
        https://docs.kumex.com/#add-margin-manually

        :param symbol:  (Mandatory)
        :type: str
        :param margin: Margin amount (min. margin amount≥0.00001667XBT）(Mandatory)
        :type: float
        :param bizNo: 	A unique ID generated by the user (Mandatory)
        :type: str
        :return:
        """
        params = {
            'symbol': symbol,
            'margin': margin,
            'bizNo': bizNo
        }
        return self._request('POST', '/api/v1/position/margin/deposit-margin', params=params)

    def get_contracts_risk_limit(self, symbol):
        """
        https://docs.kucoin.cloud/futures/#obtain-futures-risk-limit-level
        
        :param symbol:  (Mandatory)
        :type: str
        :return:
        """
        return self._request('GET', f'/api/v1/contracts/risk-limit/{symbol}')

    def change_position_risk_limit_level(self, symbol, level):
        """
        https://docs.kucoin.com/futures/#adjust-risk-limit-level
        
        :param symbol:  (Mandatory)
        :type: str
        :param level:  (Mandatory)
        :type: int
        :return:
        """
        params = {
            'symbol': symbol,
            'level': level,
        }
        return self._request('POST', '/api/v1/position/risk-limit-level/change', params=params)

    def get_fills_details(self, symbol='', orderId='', side='', type='', startAt=None, endAt=None, **kwargs):
        """
        https://docs.kumex.com/#get-fills
        :param symbol: [optional] Symbol of the contract
        :type: str
        :param orderId: List fills for a specific order only (If you specify orderId, other parameters can be ignored) [optional]
        :type: str
        :param side: [optional] buy or sell
        :type: str
        :param type: [optional] limit, market, limit_stop or market_stop
        :type: str
        :param startAt: [optional] Start time (milisecond)
        :type: int
        :param endAt: 	[optional] End time (milisecond)
        :type: str
        :param kwargs:  [optional]  currentPage , pageSize  and so on
        :return:
        {
      "currentPage":1,
      "pageSize":1,
      "totalNum":251915,
      "totalPage":251915,
      "items":[
          {
            "symbol": "XBTUSDTM",  //Ticker symbol of the contract
            "tradeId": "5ce24c1f0c19fc3c58edc47c",  //Trade ID
            "orderId": "5ce24c16b210233c36ee321d",  // Order ID
            "side": "sell",  //Transaction side
            "liquidity": "taker",  //Liquidity- taker or maker
            "price": "8302",  //Filled price
            "size": 10,  //Filled amount
            "value": "0.001204529",  //Order value
            "feeRate": "0.0005",  //Floating fees
            "fixFee": "0.00000006",  //Fixed fees
            "feeCurrency": "XBT",  //Charging currency
            "stop": "",  //A mark to the stop order type
            "fee": "0.0000012022",  //Transaction fee
            "orderType": "limit",  //Order type
            "tradeType": "trade",  //Trade type (trade, liquidation or ADL)
            "createdAt": 1558334496000  //Time the order created
            "settleCurrency": "XBT", //settlement currency
            "tradeTime": 1558334496000000000 //trade time in nanosecond
          }
      ]
    }
        """
        params = {}
        if symbol:
            params['symbol'] = symbol
        if orderId:
            params['orderId'] = orderId
        if side:
            params['side'] = side
        if type:
            params['type'] = type
        if startAt:
            params['startAt'] = startAt
        if endAt:
            params['endAt'] = endAt
        if kwargs:
            params.update(kwargs)

        return self._request('GET', '/api/v1/fills', params=params)

    def get_recent_fills(self):
        """
        https://docs.kumex.com/#recent-fills

        :return:
        [{
         "symbol": "XBTUSDTM",  //Ticker symbol of the contract
         "tradeId": "5ce24c1f0c19fc3c58edc47c",  //Trade ID
         "orderId": "5ce24c16b210233c36ee321d",  //Order ID
         "side": "sell",  //Transaction side
         "liquidity": "taker",  // Liquidity-taker or maker
         "price": "8302",  //Filled price
         "size": 10,  //Filled amount
         "value": "0.001204529",  //Order value
         "feeRate": "0.0005",  //Floating rate
         "fixFee": "0.00000006",  //Fixed fees
         "feeCurrency": "XBT",  //Charging currency
         "stop": "",  //A mark to the stop order type
         "fee": "0.0000012022",  //Transaction fee
         "orderType": "limit",  //Order type
         "tradeType": "trade",  //Trade type (tradek, liquidation or ADL )
         "createdAt": 1558334496000  //Time the order created
         "settleCurrency": "XBT", //settlement currency
         "tradeTime": 1558334496000000000 //trade time in nanosecond
        },....]
        """
        return self._request('GET', '/api/v1/recentFills')

    def get_open_order_details(self, symbol):
        """
        https://docs.kumex.com/#active-order-value-calculation

        :param symbol: interest symbol (Mandatory)
        :type: str
        :return:
        {'openOrderSellSize': 0, 'openOrderBuyCost': '0.170008023', 'openOrderBuySize': 1390, 'openOrderSellCost': '0'  "settleCurrency": "XBT" }
        """
        params = {
            'symbol': symbol,
        }

        return self._request('GET', '/api/v1/openOrderStatistics', params=params)

    def create_limit_order(self, symbol, side, lever, size, price, clientOid='', **kwargs):
        """
        Place Limit Order Functions

        https://docs.kumex.com/#place-an-order

        :param symbol: interest symbol (Mandatory)
        :type: str
        :param side: place direction buy or sell (Mandatory)
        :type: str
        :param lever: Leverage of the order (Mandatory)
        :type: str
        :param size: Order size. Must be a positive number (Mandatory)
        :type: str
        :param price: Limit price (Mandatory)
        :type: str
        :param clientOid: Unique order id created by users to identify their orders, e.g. UUID, Only allows numbers,
         characters, underline(_), and separator(-) (Mandatory)
        :type: str
        :param kwargs:  Fill in parameters with reference documents
        :return: {'orderId': '5d9ee461f24b80689797fd04'}
        """
        params = {
            'symbol': symbol,
            'size': size,
            'side': side,
            'price': price,
            'leverage': lever,
            'type': 'limit'
        }
        if not clientOid:
            clientOid = self.return_unique_id
        params['clientOid'] = clientOid
        if kwargs:
            params.update(kwargs)

        return self._request('POST', '/api/v1/orders', params=params)

    def create_market_order(self, symbol, side, lever, clientOid='', **kwargs):
        """
        Place Market Order Functions
        https://www.kucoin.com/docs/rest/futures-trading/orders/place-order
        :param symbol: interest symbol (Mandatory)
        :type: str
        :param side: place direction buy or sell (Mandatory)
        :type: str
        :param lever: Leverage of the order (Mandatory)
        :type: str
        :param clientOid: Unique order id created by users to identify their orders, e.g. UUID, Only allows numbers,
         characters, underline(_), and separator(-) (Mandatory)
        :type: str
        :param kwargs:  Fill in parameters with reference documents
        :return: {'orderId': '5d9ee461f24b80689797fd04'}
        """
        params = {
            'symbol': symbol,
            'side': side,
            'leverage': lever,
            'type': 'market'

        }
        if not clientOid:
            clientOid = self.return_unique_id
        params['clientOid'] = clientOid
        if kwargs:
            params.update(kwargs)

        return self._request('POST', '/api/v1/orders', params=params)

    def place_order_test(self, symbol, side, lever, type, clientOid='', **kwargs):
        """
        Place Order Test
        https://www.kucoin.com/docs/rest/futures-trading/orders/place-order-test
        """
        params = {
            'symbol': symbol,
            'side': side,
            'leverage': lever,
            'type': type

        }
        if not clientOid:
            clientOid = self.return_unique_id
        params['clientOid'] = clientOid
        if kwargs:
            params.update(kwargs)
        return self._request('POST', '/api/v1/orders/test', params=params)

    def cancel_order(self, orderId):
        """
        https://docs.kumex.com/#cancel-an-order

        :param orderId: str  (Mandatory)
        :return:{'cancelledOrderIds': ['5d9ee77825aa3809494eac87']}
        """
        return self._request('DELETE', f'/api/v1/orders/{orderId}')

    def cancel_all_limit_order(self, symbol):
        """
        https://docs.kumex.com/#limit-order-mass-cancelation

        :param symbol: str  (Mandatory)
        :return:{'cancelledOrderIds': ['5d9d684ef24b806897632962', '5d9dd98725aa380949298eb0', ...]}
        """
        params = {
            'symbol': symbol
        }
        return self._request('DELETE', '/api/v1/orders', params=params)

    def cancel_all_stop_order(self, symbol):
        """
        https://docs.kumex.com/#stop-order-mass-cancelation

        :param symbol: str  (Mandatory)
        :return:{'cancelledOrderIds': ['5d9d684ef24b806897632962', '5d9dd98725aa380949298eb0', ...]}
        """
        params = {
            'symbol': symbol
        }
        return self._request('DELETE', '/api/v1/stopOrders', params=params)

    def get_order_list(self, **kwargs):
        """
        https://docs.kumex.com/#get-order-list

         return List your current orders.

        :param kwargs: [optional] symbol, status, side, type, startAt, endAt, currentPage , pageSize  and so on
        :return:
        {
          "currentPage": 1,
          "pageSize": 100,
          "totalNum": 1000,
          "totalPage": 10,
          "items": [
            {
              "id": "5cdfc138b21023a909e5ad55", //Order ID
              "symbol": "XBTUSDTM",  //Ticker symbol of the contract
              "type": "limit",   //Order type, market order or limit order
              "side": "buy",  //Transaction side
              "price": "3600",  //Order price
              "size": 20000,  //Order quantity
              "value": "56.1167227833",  //Order value
              "dealValue": "0",  //Value of the executed orders
              "dealSize": 0,  //Executed order quantity
              "stp": "",  //Self trade prevention types
              "stop": "",  //Stop order type (stop limit or stop market)
              "stopPriceType": "",  //Trigger price type of stop orders
              "stopTriggered": false,  //Mark to show whether the stop order is triggered
              "stopPrice": null,  //Trigger price of stop orders
              "timeInForce": "GTC",  //Time in force policy type
              "postOnly": false,  // Mark of post only
              "hidden": false,  //Mark of the hidden order
              "iceberg": false,  //Mark of the iceberg order
              "visibleSize": null,  //Visible size of the iceberg order
              "leverage": "20",  //Leverage of the order
              "forceHold": false,  //A mark to forcely hold the funds for an order
              "closeOrder": false, //A mark to close the position
              "reduceOnly": false,  //A mark to reduce the position size only
              "clientOid": "5ce24c16b210233c36ee321d",  //Unique order id created by users to identify their orders
              "remark": null,  //Remark of the order
              "isActive": true,  //Mark of the active orders
              "cancelExist": false,  //Mark of the canceled orders
              "createdAt": 1558167872000  //Time the order created
              "settleCurrency": "XBT", //settlement currency
              status": "open", //order status: “open” or “done”
             "updatedAt": 1558167872000, //last update time
              "orderTime": 1558167872000000000 //order create time in nanosecond
            }
          ]
        }
        """
        params = {}
        if kwargs:
            params.update(kwargs)

        return self._request('GET', '/api/v1/orders', params=params)

    def get_open_stop_order(self, **kwargs):
        """
        https://docs.kumex.com/#get-untriggered-stop-order-list

        :param kwargs:c
        :return:
        {
      "currentPage": 1,
      "pageSize": 100,
      "totalNum": 1000,
      "totalPage": 10,
      "items": [
        {
            "id": "5cdfc138b21023a909e5ad55", //Order ID
            "symbol": "XBTUSDTM",  //Ticker symbol of the contract
            "type": "limit",   //Order type, market order or limit order
            "side": "buy",  //Transaction side
            "price": "3600",  //Order price
            "size": 20000,  //Order quantity
            "value": "56.1167227833",  //Order value
            "dealValue": "0",  //Value of the executed orders
            "dealSize": 0,  //Executed order quantity
            "stp": "",  //Self trade prevention types
            "stop": "",  //Stop order type (stop limit or stop market)
            "stopPriceType": "",  //Trigger price type of stop orders
            "stopTriggered": false,  //Mark to show whether the stop order is triggered
            "stopPrice": null,  //Trigger price of stop orders
            "timeInForce": "GTC",  //Time in force policy type
            "postOnly": false,  //Mark of post only
            "hidden": false,  //Mark of the hidden order
            "iceberg": false,  //Mark of the iceberg order
            "visibleSize": null,  //Visible size of the iceberg order
            "leverage": "20",  //Leverage of the order
            "forceHold": false,  //A mark to forcely hold the funds for an order
            "closeOrder": false, //A mark to close the position
            "reduceOnly": false,  //A mark to reduce the position size only
            "clientOid": "5ce24c16b210233c36ee321d",  //Unique order id created by users to identify their orders
            "remark": null,  //Remark of the order
            "isActive": true,  //Mark of the active orders
            "cancelExist": false,  //Mark of the canceled orders
            "createdAt": 1558167872000  //Time the order created
            "settleCurrency": "XBT", //settlement currency
            "status": "open", //order status: “open” or “done”
            "updatedAt": 1558167872000 //last update time
        }
      ]
    }
        """
        params = {}
        if kwargs:
            params.update(kwargs)

        return self._request('GET', '/api/v1/stopOrders', params=params)

    def get_24h_done_order(self, **kwargs):
        """
        https://docs.kumex.com/#get-list-of-orders-completed-in-24h
        :param kwargs: [optional] currentPage , pageSize  and so on
        :return:
         {
      "currentPage": 1,
      "pageSize": 1,
      "totalNum": 153408,
      "totalPage": 15340,
      "items": [
          {
            "id": "5cdfc138b21023a909e5ad55", //Order ID
            "symbol": "XBTUSDTM",  //Ticker symbol of the contract
            "type": "limit",   //Order type, market order or limit order
            "side": "buy",  //Transaction side
            "price": "3600",  //Order price
            "size": 20000,  //Order quantity
            "value": "56.1167227833",  //Order value
            "dealValue": "56.1167227833",  //Value of the executed orders
            "dealSize": 20000,  //Executed order quantity
            "stp": "",  //Self trade prevention types
            "stop": "",  //Stop order type (stop limit or stop market)
            "stopPriceType": "",  //Trigger price type of stop orders
            "stopTriggered": true,  //Mark to show whether the stop order is triggered
            "stopPrice": null,  //Trigger price of stop orders
            "timeInForce": "GTC",  //Time in force policy type
            "postOnly": false,  //Mark of post only
            "hidden": false,  //Mark of the hidden order
            "iceberg": false,  //Mark of the iceberg order
            "visibleSize": null,  // Visible size of the iceberg order
            "leverage": "20",  //Leverage of the order
            "forceHold": false,  //A mark to forcely hold the funds for an order
            "closeOrder": false, //A mark to close the position
            "reduceOnly": false,  //A mark to reduce the position size only
            "clientOid": "5ce24c16b210233c36ee321d",  //Unique order id created by users to identify their orders
            "remark": null,  //Remark of the order
            "isActive": false,  //Mark of the active orders
            "cancelExist": false,  //Mark of the canceled orders
            "createdAt": 1558167872000  //Time the order created
            "settleCurrency": "XBT", //settlement currency
            "status": "done", //order status: “open” or “done”
            "updatedAt": 1558167872000, //last update time
            "orderTime": 1558167872000000000 //order create time in nanosecond
          }
      ]
    }
        """
        params = {}
        if kwargs:
            params.update(kwargs)

        return self._request('GET', '/api/v1/recentDoneOrders', params=params)

    def get_order_details(self, orderId):
        """
        https://docs.kumex.com/#get-details-of-a-single-order
        Get a single order by order id (including a stop order).
        :param orderId: str
        :return:
        {
          "id": "5cdfc138b21023a909e5ad55", //Order ID
          "symbol": "XBTUSDTM",  //Ticker symbol of the contract
          "type": "limit",   //Order type, market order or limit order
          "side": "buy",  //Transaction side
          "price": "3600",  //Order price
          "size": 20000,  //Order quantity
          "value": "56.1167227833",  //Order value
          "dealValue": "56.1167227833",  //Value of the executed orders
          "dealSize": 20000,  //Executed order quantity
          "stp": "",  //Self trade prevention types
          "stop": "",  //Stop order type (stop limit or stop market)
          "stopPriceType": "",  //Trigger price type of stop orders
          "stopTriggered": true,  //Mark to show whether the stop order is triggered
          "stopPrice": null,  //Trigger price of stop orders
          "timeInForce": "GTC",  //Time in force policy types
          "postOnly": false,  //Mark of post only
          "hidden": false,  //Mark of the hidden order
          "iceberg": false,  //Mark of the iceberg order
          "visibleSize": null,  //Visible size of the iceberg order
          "leverage": "20",  //Leverage of the order
          "forceHold": false,  //A mark to forcely hold the funds for an order
          "closeOrder": false, //A mark to close the position
          "reduceOnly": false,  //A mark to reduce the position size only
          "clientOid": "5ce24c16b210233c36ee321d",  //Unique order id created by users to identify their orders
          "remark": null,  //Remarks of the order
          "isActive": false,  //Mark of the active orders
          "cancelExist": false,  //Mark of the canceled orders
          "createdAt": 1558167872000  //Time the order created
          "settleCurrency": "XBT", //settlement currency
          "status": "done", //order status: “open” or “done”
          "updatedAt": 1558167872000, //last update time
          "orderTime": 1558167872000000000 //order create time in nanosecond
        }
        """
        return self._request('GET', f'/api/v1/orders/{orderId}')

    def get_public_funding_history(self, symbol, fr, to):
        """
        Get Public Funding History
        Query the funding rate at each settlement time point within a certain time range of the corresponding contract
        https://www.kucoin.com/docs/rest/futures-trading/funding-fees/get-public-funding-history
        :param symbol: Symbol of the contract
        :param fr: Start time (milisecond)
        :param to: End time (milisecond)
        :return:
          {
              "success": true,
              "code": "200",
              "msg": "success",
              "retry": false,
              "data": [
                  {
                      "symbol": "IDUSDTM",
                      "fundingRate": 0.018750,
                      "timepoint": 1702310700000
                  }
              ]
          }
        """
        params = {
            'symbol': symbol,
            'from': fr,
            'to': to,
        }
        return self._request('GET', '/api/v1/contract/funding-rates', params=params)

    def get_24h_futures_transaction_volume(self):
        """
        Get 24-hour platform futures trading volume
        https://www.kucoin.com/docs/rest/futures-trading/market-data/get-24hour-futures-transaction-volume
        :return:
        {
          "success": true,
          "code": "200",
          "msg": "success",
          "retry": false,
          "data": {
              "turnoverOf24h": 619 //24-hour platform Futures trading volume. Unit is USD
          }
        }
        """
        return self._request('GET', '/api/v1/trade-statistics')

    def cancel_order_by_clientOid(self, clientOid, symbol):
        """
        Cancel Order by clientOid
        You will receive success message once the system has received the cancellation request. The cancellation request will be processed by matching engine in sequence. To know if the request has been processed, you may check the order status or update message from the pushes.
        Response the ID created by the client (clientOid).
        If the order can not be canceled (already filled or previously canceled, etc), then an error response will indicate the reason in the message field.
        https://www.kucoin.com/docs/rest/futures-trading/orders/cancel-order-by-clientoid
        :return:
          {
            "code": "200000",
            "data": {
              "clientOid": [
                "5cdfc120b21023a909e5ad52"
              ]
            }
          }
        """
        params = {
            'symbol': symbol
        }
        return self._request('DELETE', f'/api/v1/orders/client-order/{clientOid}', params=params)


    def place_multiple_orders(self, orderList):
        """
        Place Multiple Orders
        https://www.kucoin.com/zh-hant/docs/rest/futures-trading/orders/place-multiple-orders
        You can place up to 20 orders at one time, including limit orders, market orders, and stop orders
        """
        params = orderList
        return self._request('POST', '/api/v1/orders/multi', params=params)

    def get_max_withdraw_margin(self,symbol):
        """
        Get Max Withdraw Margin
        https://www.kucoin.com/docs/rest/futures-trading/positions/get-max-withdraw-margin
        """
        params = {
            'symbol': symbol
        }
        return self._request('GET', '/api/v1/margin/maxWithdrawMargin',params=params)

    def remove_margin_manually(self,symbol,withdrawAmount):
        """
        Remove Margin Manually
        https://www.kucoin.com/docs/rest/futures-trading/positions/remove-margin-manually
        """
        params = {
            'symbol': symbol,
            'withdrawAmount':withdrawAmount
        }
        return self._request('POST', '/api/v1/margin/withdrawMargin',params=params)

    def trading_pair_actual_fee_futures(self,symbol):
        """
        Trading pair actual fee - Futures
        https://www.kucoin.com/docs/rest/funding/trade-fee/trading-pair-actual-fee-futures
        """
        params = {
            'symbol': symbol
        }
        return self._request('GET', '/api/v1/trade-fees',params=params)

    def get_positions_history(self,symbol=None,fr=None,to=None,limit=None,pageId=None):
        """
        Get Positions History
        https://www.kucoin.com/docs/rest/futures-trading/positions/get-positions-history
        """
        params = {
            'symbol': symbol,
            'from': fr,
            'to': to,
            'limit': limit,
            'pageId': pageId
        }
        params = {k: v for k, v in params.items() if v is not None}
        return self._request('GET', '/api/v1/history-positions',params=params)

    def get_max_open_size(self, symbol, price, leverage):
        """
        https://www.kucoin.com/docs/rest/futures-trading/positions/get-maximum-open-position-size
        Get Maximum Open Position Size
        Request:
        +-----------+------------+-----------+-------------------+
        | Parameter | Type       | Mandatory | Description       |
        +-----------+------------+-----------+-------------------+
        | symbol    | String     | Yes       | Contract symbol   |
        | price     | BigDecimal | Yes       | Order price       |
        | leverage  | BigDecimal | Yes       | Leverage          |
        +-----------+------------+-----------+-------------------+
        Response:
        +------------------+-----------------------+
        | Param            | Description           |
        +------------------+-----------------------+
        | symbol           | Contract symbol       |
        | maxBuyOpenSize   | Maximum buy size      |
        | maxSellOpenSize  | Maximum sell size     |
        +------------------+-----------------------+
        """

        params = {
            "symbol": symbol,
            "price": price,
            "leverage":leverage
        }
        return self._request('GET', '/api/v2/getMaxOpenSize', params=params)

    def get_margin_mode(self, symbol):
        """
        https://www.kucoin.com/docs/rest/futures-trading/positions/get-margin-mode
        Query the margin mode of the current symbol.
        Request
        +------------+----------+-----------+--------------------------------------+
        | Param      | Type     | Mandatory | Description                          |
        +------------+----------+-----------+--------------------------------------+
        | symbol     | String   | Yes       | Symbol of the contract               |
        +------------+----------+-----------+--------------------------------------+

        RESPONSES
        +------------+-------------------------------------------------------------+
        | Param      | Description                                                 |
        +------------+-------------------------------------------------------------+
        | symbol     | Symbol of the contract                                      |
        | marginMode | Margin mode: ISOLATED (isolated), CROSS (cross margin).      |
        +------------+-------------------------------------------------------------+
        """

        params = {
            'symbol' : symbol
        }
        return self._request('GET', '/api/v2/position/getMarginMode', params=params)

    def change_margin_mode(self, symbol, margin_mode):
        """
        https://www.kucoin.com/docs/rest/futures-trading/positions/modify-margin-mode
        This interface can modify the margin mode of the current symbol
        PARAMETERS
        +------------+----------+-----------+------------------------------------------------------+
        | Param      | Type     | Mandatory | Description                                          |
        +------------+----------+-----------+------------------------------------------------------+
        | symbol     | String   | Yes       | Symbol of the contract                               |
        | marginMode | String   | Yes       | Modified margin model: ISOLATED (isolated), CROSS    |
        |            |          |           | (cross margin).                                      |
        +------------+----------+-----------+------------------------------------------------------+

        RESPONSES
        +------------+-------------------------------------------------------------+
        | Param      | Description                                                 |
        +------------+-------------------------------------------------------------+
        | symbol     | Symbol of the contract                                      |
        | marginMode | Margin mode: ISOLATED (isolated), CROSS (cross margin).      |
        +------------+-------------------------------------------------------------+
        """

        params = {
            'symbol' : symbol,
            'marginMode' : margin_mode,
        }
        return self._request('POST', '/api/v2/position/changeMarginMode', params=params)


    def get_cross_user_leverage(self, symbol):
        """
        https://www.kucoin.com/docs/rest/futures-trading/positions/get-cross-margin-leverage
        PARAMETERS
        +--------+--------+-----------+--------------------------+
        | Param  | Type   | Mandatory | Description              |
        +--------+--------+-----------+--------------------------+
        | symbol | String | Yes       | Symbol of the contract   |
        +--------+--------+-----------+--------------------------+

        RESPONSES
        +----------+--------------------------+
        | Param    | Description              |
        +----------+--------------------------+
        | symbol   | Symbol of the contract   |
        | leverage | Leverage multiple        |
        +----------+--------------------------+
        """
        params = {
            'symbol': symbol,
        }
        return self._request('GET', '/api/v2/getCrossUserLeverage', params=params)

    def change_cross_user_leverage(self, symbol, leverage):
        """
        https://www.kucoin.com/docs/rest/futures-trading/positions/modify-cross-margin-leverage
        PARAMETERS
        +----------+--------+-----------+--------------------------+
        | Param    | Type   | Mandatory | Description              |
        +----------+--------+-----------+--------------------------+
        | symbol   | String | Yes       | Symbol of the contract   |
        | leverage | String | Yes       | Leverage multiple        |
        +----------+--------+-----------+--------------------------+

        RESPONSES
        +-------+----------------------+
        | Param | Description          |
        +-------+----------------------+
        | data  | Whether successful   |
        +-------+----------------------+
        """
        params = {
            'symbol': symbol,
            'leverage' : leverage,
        }
        return self._request('POST', '/api/v2/changeCrossUserLeverage', params=params)

    def place_st_order(self, symbol, side, leverage, size, price, clientOid='', **kwargs):
        """
        Place take profit and stop loss order

        https://www.kucoin.com/docs/rest/futures-trading/orders/place-take-profit-and-stop-loss-order

        Public Order Placement Request Parameters
        +------------------------+----------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Param                  | Type     | Mandatory | Description                                                                                                                                                                                   |
        +------------------------+----------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | clientOid              | String   | Yes       | Unique order id created by users to identify their orders, the maximum length cannot exceed 40, e.g. UUID. Only allows numbers, characters, underline(_), and separator(-)                     |
        | side                   | String   | Yes       | buy or sell                                                                                                                                                                                   |
        | symbol                 | String   | Yes       | A valid contract code. e.g. XBTUSDM                                                                                                                                                          |
        | leverage               | String   | Yes       | Used to calculate the margin to be frozen for the order. If you are to close the position, this parameter is not required.                                                                    |
        | type                   | String   | No        | Either limit or market. The default type is limit                                                                                                                                             |
        | remark                 | String   | No        | Remark for the order, length cannot exceed 100 UTF-8 characters                                                                                                                              |
        | triggerStopUpPrice     | String   | No        | Take profit price                                                                                                                                                                             |
        | stopPriceType          | String   | No        | Either TP, IP or MP                                                                                                                                                                           |
        | triggerStopDownPrice   | String   | No        | Stop loss price                                                                                                                                                                               |
        | reduceOnly             | boolean  | No        | A mark to reduce the position size only. Set to false by default. If set to TRUE, only the orders reducing the position size will be executed. Excess size will be canceled.                   |
        | closeOrder             | boolean  | No        | A mark to close the position. Set to false by default. If TRUE, the system will close the position and the position size will become 0. Side, Size, and Leverage fields can be left empty.     |
        | forceHold              | boolean  | No        | A mark to forcely hold the funds for an order. Set to false by default. The system will forcely freeze certain amount of funds for this order to ensure it won’t be canceled by the engine.     |
        | stp                    | String   | No        | Self trade prevention, CN, CO, CB. Not supported DC at the moment                                                                                                                            |
        +------------------------+----------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        Additional Request Parameters Required by Limit Orders
        +-------------+----------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Param       | Type     | Mandatory | Description                                                                                                                                                    |
        +-------------+----------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | price       | String   | Yes       | Limit price                                                                                                                                                    |
        | size        | Integer  | Yes       | Order size. Must be a positive number                                                                                                                          |
        | timeInForce | String   | No        | GTC, IOC (default is GTC)                                                                                                                                      |
        | postOnly    | boolean  | No        | Post only flag, invalid when timeInForce is IOC. The post-only flag ensures that the trader always pays the maker fee and provides liquidity to the order book. |
        | hidden      | boolean  | No        | Orders not displaying in the order book. When hidden is chosen, postOnly is not allowed.                                                                        |
        | iceberg     | boolean  | No        | Only visible portion of the order is displayed in the order book. When iceberg is chosen, postOnly is not allowed.                                              |
        | visibleSize | Integer  | No        | The maximum visible size of an iceberg order                                                                                                                   |
        +-------------+----------+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

        Additional Request Parameters Required by Market Orders

        +------+---------+-----------+-----------------------------------+
        | Param| Type    | Mandatory | Description                       |
        +------+---------+-----------+-----------------------------------+
        | size | Integer | No        | Amount of contracts to buy or sell|
        +------+---------+-----------+-----------------------------------+

        RESPONSES
        +-----------+------------------+
        | Param     | Description      |
        +-----------+------------------+
        | orderId   | Order ID.        |
        | clientOid | Client order ID. |
        +-----------+------------------+
        """
        params = {
            'symbol': symbol,
            'size': size,
            'side': side,
            'price': price,
            'leverage': leverage,
        }
        if not clientOid:
            clientOid = self.return_unique_id
        params['clientOid'] = clientOid
        if kwargs:
            params.update(kwargs)
        return self._request('POST', '/api/v1/st-orders', params=params)