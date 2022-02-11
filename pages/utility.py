import requests as rq
import pandas as pd
from pandas.io.json import json_normalize
import san
from lunarcrush import LunarCrush


def getTickerList():
    response=rq.get("https://api.coinpaprika.com/v1/coins")
    test=pd.DataFrame(response.json())
    td=test.head(50)
    td.symbol


lc = LunarCrush()
btc = lc.get_assets(symbol=['BTC'], data_points=7, interval='day')

response=rq.get("https://api.coinpaprika.com/v1/tickers")
test=pd.DataFrame(response.json())
td=test

san.ApiConfig.api_key = 'ky5sc6dq6ezpap5j_sthp7fobmdy277ya'
sentiment = san.get("sentiment_balance_twitter/santiment",
                    from_date="2020-06-01",
                    to_date="2021-06-05",
                    interval="1d")
    
TickSym = getTickerList()
print(TickSym['symbols'])
# # print(td)
# print(sentiment)
# print(btc)
