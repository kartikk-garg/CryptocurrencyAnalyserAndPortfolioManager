from attr import attr
import requests as rq
import pandas as pd
from pandas.io.json import json_normalize
import json
from lunarcrush import LunarCrush
from pytrends.request import TrendReq
import streamlit as st
import streamlit as st 
import requests
from lunarcrush import LunarCrush
import pandas as pd

lc = LunarCrush()

def getDetailsByID(idname):
    link="https://api.coinpaprika.com/v1/coins/"+idname
    response=rq.get(link)
    pd.json_normalize(response.json())[['symbol','name','type','platform','description','started_at','development_status',
                    'links.explorer', 'links.facebook','links.reddit', 'links.source_code', 'links.website', 'links.youtube',]]
                    
def theTweet(url):
    api="https://publish.twitter.com/oembed?url={}".format(url)
    response=requests.get(api)
    res = response.json()["html"] 
    return res

def feeds(symbol):
    resS = []
    feed = lc.get_feeds(symbol)
    urls=pd.json_normalize(feed['data'])['url']

    for i in range(min(5,urls.size)):
        resS.append(theTweet(urls[i]))
        
    return resS

# @st.experimental_memo
def compMultiCryptoBasesAttr(symbols, attr):
    lc = LunarCrush()
    data = lc.get_assets(symbol=symbols, data_points=365, interval='year')
    df=pd.DataFrame()
    j=0
    for i in symbols:
        df[i]=pd.json_normalize(data['data'][j]['timeSeries'])[attr]
        j+=1

    return df
    # st.line_chart(df)


# @st.experimental_memo
def data(sym1):
    data = lc.get_assets(symbol=sym1, data_points=365, interval='year')
    df=pd.json_normalize(data['data'][0]['timeSeries'])
    return df

# @st.experimental_memo
def data2(sym1, sym2):
    data = lc.get_assets(symbol=[sym1,sym2], data_points=365, interval='year')
    df=pd.json_normalize(data['data'][0]['timeSeries'])
    return df

def perChange(sym1, arg):
    # data = lc.get_assets(symbol=[sym1], data_points=365, interval='year')
    # df10=pd.json_normalize(data['data'][0]['timeSeries'])
    df10=data(sym1)
    df=pd.DataFrame(columns=['Price',arg])
    df['Price']=(df10['close']-df10['open'])/df10['open']*100
    t1=df10[arg][1:].reset_index(drop=True)
    t2=df10[arg]
    df[arg]=(t2-t1)/t1*100
    df.dropna(inplace=True)
    return df

def dataForSingleCoinDoubleAttribute(sym1, attr1, attr2):
    # data = lc.get_assets(symbol=[sym1], data_points=100, interval='year')
    # df=pd.json_normalize(data['data'][0]['timeSeries'])
    df = data(sym1)
    return df[[attr1, attr2]]

def dataForOne(sym1, attr):
    # data = lc.get_assets(symbol=[sym1], data_points=100, interval='year')
    # df=pd.json_normalize(data['data'][0]['timeSeries'])
    
    df = data(sym1)

    return df[attr]
    # st.line_chart(df[attr])

def compBtwTwoCoinsBasesAttribute(sym1, sym2, attr):
    data = lc.get_assets(symbol=[sym1,sym2], data_points=365, interval='year')
    df10=pd.json_normalize(data['data'][0]['timeSeries'])
    # df10 = data2(sym1, sym2)
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
    # df10 = data2(sym1, sym2)

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
    # data = lc.get_assets(symbol=[sym1], data_points=365, interval='year')
    # df=pd.json_normalize(data['data'][0]['timeSeries'])
    df = data(sym1)
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
    data = lc.get_assets(symbol=symbols, data_points = dataPoints, interval='month')
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
    

