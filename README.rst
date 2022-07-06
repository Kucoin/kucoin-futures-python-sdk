===============================
Welcome to kucoin-futures-python-sdk
===============================

.. image:: https://img.shields.io/pypi/l/python-kumex.svg
    :target: https://github.com/Kucoin/kucoin_futures-python-sdk/blob/master/LICENSE

.. image:: https://img.shields.io/badge/python-3.6%2B-green
    :target: https://pypi.org/project/python-kumex


Features
--------

- Implementation of REST endpoints
- Simple handling of authentication
- Response exception handling
- Implement websockets (note only python3.6+)

update
----------
- 2022 06/24

Quick Start
-----------

Register an account with `KuCoin_Futures <https://futures.kucoin.com/signup?utm=api_github>`_.

To test on the Sandbox  with `KuCoin_Futures Sandbox <https://sandbox-futures.kucoin.com>`_.

`Generate an API Key <https://futures.kucoin.com/api/create>`_
or `Generate an API Key in Sandbox <https://sandbox-futures.kucoin.com/api/create?utm=api_github>`_ and enable it.
Note:API key can only be generated after logging in.

.. code:: bash

    pip install kucoin-futures-python

.. code:: python

    #  MarketData
    from kucoin_futures.client import FuturesApi
    client = FuturesApi(url='https://api-futures.kucoin.com')
    # client = Market()
    # or connect to Sandbox
    # client = Market(url='https://api-sandbox-futures.kucoin.com')
    # client = Market(is_sandbox=True)

    # get order_book `GET /api/v2/order-book`
    order_book = client.get_order_book(symbol="BTCUSDTM")
    print(order_book)

    # get Best Maker `GET /api/v2/ticker/bookTicker`
    best_maker = client.best_maker(symbol="BTCUSDTM")

    # Trade
    client = FuturesApi(key='', secret='', passphrase='', is_sandbox=False, url='')

    # or connect to Sandbox
    # client = FuturesApi(api_key, api_secret, api_passphrase, is_sandbox=True)

    # place a limit buy order
    order = client.order_placement(
            symbol="BTCUSDTM",
            # clientOid=uuid.uuid1().hex,
            side="BUY",
            typ="LIMIT",
            price=1,
            size=1,
        )
    print(order)


Websockets
----------

.. code:: python

    import asyncio
    from kucoin_futures.client import WsToken
    from kucoin_futures.ws_client import KucoinFuturesWsClient


    async def main():
        test_topic = '/futuresMarket/level2Depth50:BTCUSDTM'
        async def deal_msg(msg):
            if msg.get('topic','') == test_topic:
                print(msg)

        # is public
        # client = WsToken()
        # is private
        client = WsToken(key='', secret='', passphrase='', is_sandbox=False, url='')
        # is sandbox
        # client = WsToken(is_sandbox=True)
        ws_client = await KucoinFuturesWsClient.create(loop, client, deal_msg, private=False)
        await ws_client.subscribe(test_topic)
        while True:
            await asyncio.sleep(60)


    if __name__ == "__main__":
        loop = asyncio.get_event_loop_policy().get_event_loop()
        loop.run_until_complete(main())
