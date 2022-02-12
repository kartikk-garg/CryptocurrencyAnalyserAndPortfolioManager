import streamlit as st
from pages import utility

def app():
    coins = st.multiselect("Select Coin", utility.symbols[:3000])
    col1,col2 = st.columns(2)
    col1.multiselect("Timeframe", ["1D", "1W", "1M", "3M", "6M", "1Y"])
    # col2.write("test")
# make comparison graph for selected currencies
# i.e. percentage change in price everyday
# if you want to limit comparison between 2 coins
# make graph for comparison between 2 coins