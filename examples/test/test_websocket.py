import asyncio
from kucoin_futures.client import WsToken
from kucoin_futures.ws_client import KucoinFuturesWsClient
import os
import sys

current_path = os.path.abspath(os.path.dirname(__file__))
root = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
sys.path.append(root)
from examples_config import gloabl_examples_api_config


async def deal_msg(msg):
    print(msg)


async def test_private():

    client = WsToken(**gloabl_examples_api_config)
    ws_client = await KucoinFuturesWsClient.create(None,
                                            client,
                                            deal_msg,
                                            private=True)
    await ws_client.subscribe('/futuresTrade/orders')
    while True:
        await asyncio.sleep(60)


async def test_public():

    client = WsToken(**gloabl_examples_api_config)
    ws_client = await KucoinFuturesWsClient.create(None,
                                            client,
                                            deal_msg,
                                            private=False)
    await ws_client.subscribe('/futuresMarket/level2Depth50:BTCUSDTM')
    while True:
        await asyncio.sleep(60)

async def main():
        test_topic = '/futuresMarket/level2Depth50:BTCUSDTM'
        async def deal_msg(msg):
            if msg.get('topic','') == test_topic:
                print(msg)

        # is public
        # client = WsToken()
        # is private
        # client = WsToken(key='', secret='', passphrase='', is_sandbox=False, url='')
        client = WsToken(**gloabl_examples_api_config)
        # is sandbox
        # client = WsToken(is_sandbox=True)
        ws_client = await KucoinFuturesWsClient.create(loop, client, deal_msg, private=False)
        await ws_client.subscribe(test_topic)
        while True:
            await asyncio.sleep(60)

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
