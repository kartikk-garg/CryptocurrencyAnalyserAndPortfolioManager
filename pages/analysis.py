import streamlit as st
from pages import utility

def app():

    symbols = st.multiselect("Select Coin(s)", utility.symbols[:3000])

    if len(symbols):
        
        st.header("Price")
        closedf = utility.compMultiCryptoBasesAttr(symbols, "close")
        st.area_chart(closedf)

        st.header("Volume")
        volumedf = utility.compMultiCryptoBasesAttr(symbols, "volume")
        st.bar_chart(volumedf)

        st.header("Volatility")
        volatilitydf = utility.compMultiCryptoBasesAttr(symbols, "volatility")
        st.line_chart(volatilitydf)

        st.header("Percent Change 24h")
        perChange24hdf = utility.compMultiCryptoBasesAttr(symbols, "percent_change_24h")
        st.bar_chart(perChange24hdf)

        st.header("Market Dominance")
        marketdominancedf = utility.compMultiCryptoBasesAttr(symbols, "market_dominance")
        st.line_chart(marketdominancedf)
        # df = utility.percChangeBtwTwo(symbol[0], symbol[1])
        # st.line_chart(df)



# col2.write("test")
# make comparison graph for selected currencies
# i.e. percentage change in price everyday
# if you want to limit comparison between 2 coins
# make graph for comparison between 2 coins