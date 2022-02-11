import streamlit as st

with st.expander("Add To Portfolio", expanded=False):
    col1, col2, col3 = st.columns(3)

    with col1:
        coin = st.selectbox('Coin', ["BTC", "ETH"])

    with col2:
        quantity = st.number_input('Quantity')

    with col3:
        price = st.number_input('Price')    
    

