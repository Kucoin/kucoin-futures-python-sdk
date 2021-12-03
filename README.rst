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
- 2021 12/01

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
    from kucoin_futures.client import Market
    client = Market(url='https://api-futures.kucoin.com')
    # client = Market()
    # or connect to Sandbox
    # client = Market(url='https://api-sandbox-futures.kucoin.com')
    # client = Market(is_sandbox=True)

    # get l3_order_book
    l3_depth = client.l3_order_book('XBTUSDM')

    # get l2_order_book
    l2_depth = client.l2_order_book('XBTUSDM')

    # get symbol ticker
    klines = client.get_ticker("XBTUSDM")

    # get symbol ticker
    server_time = client.get_server_timestamp()

    api_key = '<api_key>'
    api_secret = '<api_secret>'
    api_passphrase = '<api_passphrase>'

    # Trade
    from kucoin_futures.client import Trade
    client = Trade(key='', secret='', passphrase='', is_sandbox=False, url='')

    # or connect to Sandbox
    # client = Trade(api_key, api_secret, api_passphrase, is_sandbox=True)

    # place a limit buy order
    order_id = client.create_limit_order('XBTUSDM', 'buy', '1', '30', '8600')

    # place a market buy order   Use cautiously
    order_id = client.create_market_order('XBTUSDM', 'buy', '1')

    # cancel limit order 
    client.cancel_order('5bd6e9286d99522a52e458de')

    # cancel all limit order 
    client.cancel_all_limit_order('XBTUSDM')

    # User
    from kucoin_futures.client import User
    client = User(api_key, api_secret, api_passphrase)

    # or connect to Sandbox
    # client = User(api_key, api_secret, api_passphrase, is_sandbox=True)

    address = client.get_withdrawal_quota('XBT')

Websockets
----------

.. code:: python

    import asyncio
    from kucoin_futures.client import WsToken
    from kucoin_futures.ws_client import KucoinFuturesWsClient


    async def main():
        async def deal_msg(msg):
            if msg['topic'] == '/contractMarket/level2:XBTUSDM':
                print(f'Get XBTUSDM Ticker:{msg["data"]}')
            elif msg['topic'] == '/contractMarket/level3:XBTUSDTM':
                print(f'Get XBTUSDTM level3:{msg["data"]}')

        # is public
        # client = WsToken()
        # is private
        client = WsToken(key='', secret='', passphrase='', is_sandbox=False, url='')
        # is sandbox
        # client = WsToken(is_sandbox=True)
        ws_client = await KucoinFuturesWsClient.create(loop, client, deal_msg, private=False)
        await ws_client.subscribe('/contractMarket/level2:XBTUSDM')
        await ws_client.subscribe('/contractMarket/level3:XBTUSDM')
        while True:
            await asyncio.sleep(60, loop=loop)


    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
