import streamlit as st
from pages import utility
import json

def app():
    st.write("Portfolio")
    coins = {}
    with st.form("Add To Portfolio", clear_on_submit=False): 
        with st.expander("Add To Portfolio", expanded=False):
            col1, col2, col3 = st.columns(3)

            with col1:
                coin = st.selectbox("Coin", utility.symbols[:3000])

            with col2:
                quantity = st.number_input('Quantity')

            with col3:
                price = st.number_input('Price')

            submitted = st.form_submit_button("Add")
        
        if submitted:  
            
            coinMetrics = {}
            
            coinMetrics['Ticker'] = coin
            coinMetrics['Quantity'] = quantity
            coinMetrics['Price'] = price
            coinMetrics['TotalPrice'] = price*quantity

            coins = utility.coinDict(coinMetrics)

    
    st.json(coins)
    
    

    
