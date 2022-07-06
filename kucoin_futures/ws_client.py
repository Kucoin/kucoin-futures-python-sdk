#!/usr/bin/python
# -*- coding:utf-8 -*-
from kucoin_futures.websocket.websocket import ConnectWebsocket
import asyncio


class KucoinFuturesWsClient(object):
    """
    https://docs.kumex.com/#websocket-2
    """

    def __init__(self):
        self._callback = None
        self._conn = None
        self._loop = None
        self._client = None
        self._private = False
        self._topics = set()

    @classmethod
    async def create(cls, loop, client, callback, private=False):
        self = KucoinFuturesWsClient()
        loop = loop if loop else asyncio.get_running_loop()
        self._loop = loop
        self._client = client
        self._private = private
        self._callback = callback
        self._conn = ConnectWebsocket(loop, self._client, self._recv, private)
        return self

    async def _recv(self, msg):
        if 'data' in msg:
            await self._callback(msg)

    async def subscribe(self, topic):
        """Subscribe to a channel
        :param topic: required
        :type topic: str
        :returns: None
        """

        req_msg = {
            'type': 'subscribe',
            'topic': topic,
            'response': True
        }
        self._conn.topics.append(topic)
        await self._conn.send_message(req_msg)

    async def unsubscribe(self, topic):
        """Unsubscribe from a topic

        :param topic: required
        :type topic: str
        :returns: None
        """

        req_msg = {
            'type': 'unsubscribe',
            'topic': topic,
            'response': True
        }
        self._conn.topics.remove(topic)
        await self._conn.send_message(req_msg)
