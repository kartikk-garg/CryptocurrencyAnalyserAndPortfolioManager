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
    response = rq.get("https://api.coinpaprika.com/v1/coins")
    test=pd.DataFrame(response.json())
    td=test.head(50)
    td.symbol

def lunarData(symbols, dataPoints = 10 ):
    lc = LunarCrush()
    data = lc.get_assets(symbol=symbols, data_points = dataPoints, interval='month')
    df=pd.json_normalize(data['data'][0]['timeSeries'])
    return df

def socialData(symbol):
    lc = LunarCrush()
    
    influencers = lc.get_influencers(symbol)
    influencers = json.dumps(influencers)

    feed = lc.get_feeds(symbol)
    feed = json.dumps(feed)

    return influencers, feed
    

def googleTrends(coin):
    pytrends = TrendReq(hl='en-US', tz=360) 
    pytrends.build_payload(kw_list=["BTC"])
    related_queries = pytrends.related_queries()
    related_queries.values()

def coinDict(coinMetrics):
    coinDict = {}
    coinDict[coinMetrics['Ticker']] = coinMetrics
    coinDict = json.dumps(coinDict)
    return coinDict


df = allCoinsData()
symbols = df['symbol']


# san.ApiConfig.api_key = 'ky5sc6dq6ezpap5j_sthp7fobmdy277ya'
# sentiment = san.get("sentiment_balance_twitter/santiment",
#                     from_date="2020-06-01",
#                     to_date="2021-06-05",
#                     interval="1d")
    

