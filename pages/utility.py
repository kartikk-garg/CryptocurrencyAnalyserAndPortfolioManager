import requests as rq
import pandas as pd
from pandas.io.json import json_normalize
import san
import json
from lunarcrush import LunarCrush
from pytrends.request import TrendReq

def allCoinsData():
    response=rq.get("https://api.coinpaprika.com/v1/tickers")
    df=pd.json_normalize(response.json())
    return df

def getTickerList():
    response=rq.get("https://api.coinpaprika.com/v1/coins")
    test=pd.DataFrame(response.json())
    td=test.head(50)
    td.symbol

def socialData(symbol):
    lc = LunarCrush()
    data = lc.get_assets(symbol=[symbol], data_points=7, interval='day')
    data = json.dumps(data)
    return data

def googleTrends(coin):
    pytrends = TrendReq(hl='en-US', tz=360) 
    pytrends.build_payload(kw_list=["BTC"])
    related_queries = pytrends.related_queries()
    related_queries.values()

df = allCoinsData()
symbols = df['symbol']


# san.ApiConfig.api_key = 'ky5sc6dq6ezpap5j_sthp7fobmdy277ya'
# sentiment = san.get("sentiment_balance_twitter/santiment",
#                     from_date="2020-06-01",
#                     to_date="2021-06-05",
#                     interval="1d")
    

