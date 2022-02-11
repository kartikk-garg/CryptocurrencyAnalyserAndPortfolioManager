import streamlit as st
import requests as rq
import pandas as pd
import matplotlib.pyplot as plt


add_selectbox = st.sidebar.selectbox(
    "components",
    ("Home", "Portfolio", "About Us", "How To Use")
)

with st.expander("Add To Portfolio", expanded=False):
    col1, col2, col3 = st.columns(3)

    with col1:
        coin = st.selectbox('Coin', ["BTC", "ETH"])

    with col2:
        quantity = st.number_input('Quantity')

    with col3:
        price = st.number_input('Price')    
    


response=rq.get("https://api.coinpaprika.com/v1/tickers")
st.json(rq)
test=pd.json_normalize(response.json())
test[['rank','name','circulating_supply','total_supply','quotes.USD.price','quotes.USD.volume_24h_change_24h','quotes.USD.percent_change_30d']]

# fig1, ax1 = plt.subplots()
# ax1.pie(test['quotes.USD.market_cap'].head(), labels=test['name'].head(), autopct='%1.1f%%',
#         shadow=True, startangle=90)
