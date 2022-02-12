import streamlit as st
from pages import utility

def app():   
    col1, col2 = st.columns((2,1))
    df = utility.df[['rank','name','quotes.USD.price','quotes.USD.percent_change_24h','quotes.USD.market_cap','quotes.USD.volume_24h','quotes.USD.volume_24h_change_24h']]

    col1.header('List Of Cryptocurrencies')
    col1.dataframe(df)

    col2.header('Top 10 Gainers')
    gainers = df.sort_values(by = 'quotes.USD.percent_change_24h')[['name', 'quotes.USD.price', 'quotes.USD.percent_change_24h']][-10:]
    col2.dataframe(gainers)

    col3, col4 = st.columns((2,1))
    col4.header("Top 10 Loosers")
    loosers = df.sort_values(by = 'quotes.USD.percent_change_24h')[['name', 'quotes.USD.price', 'quotes.USD.percent_change_24h']][:10]
    col4.dataframe(loosers)

    news = utility.socialData(['BTC'])[1]

    col3.json(news)


    