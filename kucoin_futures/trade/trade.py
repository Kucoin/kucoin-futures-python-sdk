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
                "symbol": "XBTUSDM",                  //Symbol
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
            "symbol": "XBTUSDM",                              //Symbol
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
          "symbol": "XBTUSDM",                              //Symbol
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
            "symbol": "XBTUSDM",  //Ticker symbol of the contract
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
         "symbol": "XBTUSDM",  //Ticker symbol of the contract
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

        https://docs.kumex.com/#place-an-order

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
              "symbol": "XBTUSDM",  //Ticker symbol of the contract
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
            "symbol": "XBTUSDM",  //Ticker symbol of the contract
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
            "symbol": "XBTUSDM",  //Ticker symbol of the contract
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
          "symbol": "XBTUSDM",  //Ticker symbol of the contract
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



