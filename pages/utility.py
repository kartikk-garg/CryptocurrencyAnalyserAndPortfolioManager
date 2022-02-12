from attr import attr
import requests as rq
import pandas as pd
from pandas.io.json import json_normalize
import san
import json
from lunarcrush import LunarCrush
from pytrends.request import TrendReq

lc = LunarCrush()


def dataForSingleCoinDoubleAttribute(sym1, attr1, attr2):
    data = lc.get_assets(symbol=[sym1], data_points=100, interval='year')
    df=pd.json_normalize(data['data'][0]['timeSeries'])
    
    return df[[attr1, attr2]]

def dataForOne(sym1, attr):
    data = lc.get_assets(symbol=[sym1], data_points=100, interval='year')
    df=pd.json_normalize(data['data'][0]['timeSeries'])
    
    return df[attr]
    # st.line_chart(df[attr])

def compBtwTwoCoinsBasesAttribute(sym1, sym2, attr):
    data = lc.get_assets(symbol=[sym1,sym2], data_points=365, interval='year')
    df10=pd.json_normalize(data['data'][0]['timeSeries'])
    df11=pd.json_normalize(data['data'][1]['timeSeries'])
    df=pd.DataFrame()
    df[sym1]=df10[attr]
    df[sym2]=df11[attr]
    return df
    # st.line_chart(df)

def socialImpactComp(sym1,sym2):
    # lc = LunarCrush()
    data = lc.get_assets(symbol=[sym1,sym2], data_points=365, interval='year')
    df10=pd.json_normalize(data['data'][0]['timeSeries'])
    df11=pd.json_normalize(data['data'][1]['timeSeries'])
    df=pd.DataFrame(columns=[sym1,sym2])
    df['Bearish']=df10['social_impact_score']
    df['Bullish']=df11['social_impact_score']
    return df

# def test(sym1):
#     # lc = LunarCrush()
#     data = lc.get_assets(symbol=[sym1], data_points=365, interval='year')
#     df=pd.json_normalize(data['data'][0]['timeSeries'])
#     df['Bearish']=df['tweet_sentiment1']+df['tweet_sentiment2']
#     df['Bullish']=df['tweet_sentiment4']+df['tweet_sentiment5']
#     return df[['Bearish','Bullish']]
#     st.line_chart()

def bullvsbear(sym1):
    # lc = LunarCrush()
    data = lc.get_assets(symbol=[sym1], data_points=365, interval='year')
    df=pd.json_normalize(data['data'][0]['timeSeries'])
    df['tweet_sentiment1']=df['tweet_sentiment1']+df['tweet_sentiment2']
    df['tweet_sentiment5']=df['tweet_sentiment4']+df['tweet_sentiment5']
    return df[['tweet_sentiment1','tweet_sentiment5']]
    # plt.plot()

# def percChangeBtwTwo(sym1, sym2, attr):
#     # lc = LunarCrush()
#     data = lc.get_assets(symbol=[sym1,sym2], data_points=365, interval='year')
#     df10=pd.json_normalize(data['data'][0]['timeSeries'])
#     df11=pd.json_normalize(data['data'][1]['timeSeries'])
#     df=pd.DataFrame(columns=[sym1,sym2])
#     df[sym1]=(df10['close']-df10['open'])/df10['open']*100
#     df[sym2]=(df11['close']-df11['open'])/df11['open']*100
#     return df

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
    # lc = LunarCrush()
    data = lc.get_assets(symbol=[symbols], data_points = dataPoints, interval='month')
    df=pd.json_normalize(data['data'][0]['timeSeries'])
    return df

def socialData(symbol):
    # lc = LunarCrush()
    
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
    

