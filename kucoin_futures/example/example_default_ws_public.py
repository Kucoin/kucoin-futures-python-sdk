
import asyncio
from kucoin_futures.client import WsToken
from kucoin_futures.ws_client import KucoinFuturesWsClient



async def main():
    async def deal_msg(msg):
        print(msg["data"])

    # is public
    client = WsToken()
    ws_client = await KucoinFuturesWsClient.create(None, client, deal_msg, private=False)

    await ws_client.subscribe('/contractMarket/level2:XBTUSDM')
    #await ws_client.subscribe('/contractMarket/level3:XBTUSDM')
    while True:
        await asyncio.sleep(60)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
