#!/usr/bin/python
# -*- coding:utf-8 -*-

from setuptools import setup


setup(
    name='kucoin-futures-python',
    version='v1.0.6',
    packages=['kucoin_futures', 'kucoin_futures/base_request', 'kucoin_futures/marke_data', 'kucoin_futures/trade', 'kucoin_futures/user',
              'kucoin_futures/websocket', 'kucoin_futures/ws_token'],
    license="MIT",
    author='Grape',
    author_email="grape.zhang@kucoin.com",
    url='https://github.com/Kucoin/kucoin-futures-python-sdk',
    description="kucoin-futures-api-sdk",
    install_requires=['requests', 'websockets'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
