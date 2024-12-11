===============================
# Notice: SDK Deprecation
===============================
Thank you for your support and usage of this SDK. We want to inform you that **this project is no longer actively maintained or updated**. 

To ensure you have access to the latest features, improvements, and support, we recommend transitioning to our new SDK: [**KuCoin Universal SDK**](https://github.com/Kucoin/kucoin-universal-sdk).

The KuCoin Universal SDK offers:
- A unified architecture across multiple programming languages.
- Enhanced performance and stability.
- Continued support and updates.

👉 **New SDK Repository**: [https://github.com/Kucoin/kucoin-universal-sdk](https://github.com/Kucoin/kucoin-universal-sdk)

We appreciate your understanding and encourage you to migrate to the new SDK for a better development experience. Should you have any questions or require assistance, feel free to reach out to us.



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
https://github.com/Kucoin/kucoin-futures-python-sdk/releases/

Quick Start
-----------

Register an account with `KuCoin_Futures <https://futures.kucoin.com/signup?utm=api_github>`_.


`Generate an API Key <https://futures.kucoin.com/api/create>`_ and enable it.
Note:API key can only be generated after logging in.

.. code:: bash

    pip install kucoin-futures-python

.. code:: python

    #  MarketData
    from kucoin_futures.client import Market
    client = Market(url='https://api-futures.kucoin.com')
    # client = Market()


    # get l3_order_book
    l3_depth = client.l3_order_book('XBTUSDTM')

    # get l2_order_book
    l2_depth = client.l2_order_book('XBTUSDTM')

    # get symbol ticker
    klines = client.get_ticker("XBTUSDTM")

    # get symbol ticker
    server_time = client.get_server_timestamp()

    api_key = '<api_key>'
    api_secret = '<api_secret>'
    api_passphrase = '<api_passphrase>'

    # Trade
    from kucoin_futures.client import Trade
    client = Trade(key='', secret='', passphrase='',  url='')



    # place a limit buy order
    order_id = client.create_limit_order('XBTUSDTM', 'buy', '1', '30', '8600')

    # place a market buy order   Use cautiously
    order_id = client.create_market_order('XBTUSDTM', 'buy', '1')

    # cancel limit order
    client.cancel_order('5bd6e9286d99522a52e458de')

    # cancel all limit order
    client.cancel_all_limit_order('XBTUSDTM')

    # User
    from kucoin_futures.client import User
    client = User(api_key, api_secret, api_passphrase)



    address = client.get_withdrawal_quota('XBT')

Websockets
----------
- ./kucoin_futures/example/example_ws_private.py
- ./kucoin_futures/example/example_default_ws_public.py
