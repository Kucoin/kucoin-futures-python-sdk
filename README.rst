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
- 2024 02/07
 1. trade.get_public_funding_history: `Get Public Funding History <https://www.kucoin.com/docs/rest/futures-trading/funding-fees/get-public-funding-history>`_.
 2. trade.get_24h_futures_transaction_volume: `Get 24-hour platform futures trading volume <https://www.kucoin.com/docs/rest/futures-trading/market-data/get-24hour-futures-transaction-volume>`_.
 3. trade.cancel_order_by_clientOid: `Cancel Order by clientOid <https://www.kucoin.com/docs/rest/futures-trading/orders/cancel-order-by-clientoid>`_.
 4. customized websocket: ./kucoin_futures/example_customized_ws_private.py | kucoin_futures/example_customized_ws_public.py.
  - sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
 5. set api TCP_NODELAY：After instantiating the client, you can cancel the Nagle algorithm through client.TCP_NODELAY=1 (default is 0)
  - kucoin/example_client_TCP_NODELAY.py




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
- ./kucoin_futures/example_customized_ws_private.py
- ./kucoin_futures/example_customized_ws_public.py
- ./kucoin_futures/example_default_ws_public.py
