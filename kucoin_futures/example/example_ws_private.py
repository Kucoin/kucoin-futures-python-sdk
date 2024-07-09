
import asyncio
import socket
from kucoin_futures.client import WsToken
from kucoin_futures.ws_client import KucoinFuturesWsClient



async def main():
    async def deal_msg(msg):
        print(msg["data"])



    #is private
    client = WsToken(key='', secret='', passphrase='')

    ws_client = await KucoinFuturesWsClient.create(None, client, deal_msg, private=True)
    await ws_client.subscribe('/contractMarket/tradeOrders')

    while True:
        await asyncio.sleep(60)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
