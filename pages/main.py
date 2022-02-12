import streamlit as st
from pages import utility

def app():   
    col1, col2 = st.columns((2,1))
    utility.df[['rank','name','quotes.USD.price','quotes.USD.percent_change_24h','quotes.USD.market_cap','quotes.USD.volume_24h','quotes.USD.volume_24h_change_24h']]

    col1.header('List Of Cryptocurrencies')
    col1.dataframe(utility.df)

    col2.header('Top 10 Gainers')
    # sort and display coin price qand percentage change
    # top 10 gaines

    col2.header("Top 10 Loosers")
    # top 10 loosers  