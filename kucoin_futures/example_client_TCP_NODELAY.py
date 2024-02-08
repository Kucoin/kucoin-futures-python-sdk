

#  MarginData
from kucoin.client import Trade
import time


client = Trade(key='', secret='', passphrase='',
               url='https://api-futures.kucoin.com')
client.TCP_NODELAY=1
res=client.create_market_order('',',')
res2=client.cancel_order(res['orderId'])
print(res)
print(res2)
