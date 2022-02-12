import streamlit as st
from pages import utility

def app():
    # with st.expander("Analyse Currency"):
    #     symbol = st.selectbox("Select Coin", utility.symbols[:3000])
    #     if symbol:
    #         col1,col2 = st.columns(2)
    #         # Timeframe =col1.multiselect("Timeframe", ["1D", "1W", "1M", "3M", "6M", "1Y"])
    #         df = utility.lunarData(symbol)
    #         st.dataframe(df)

    #         st.header("Price")
    #         closedf = utility.dataForOne(symbol, "close")
    #         st.area_chart(closedf)

    #         st.header("Volume")
    #         volumedf = utility.dataForOne(symbol, "volume")
    #         st.bar_chart(volumedf)

    #         st.header("Volatility")
    #         volatilitydf = utility.dataForOne(symbol, "volatility")
    #         st.line_chart(volatilitydf)

    #         st.header("Percent Change 24h")
    #         perChange24hdf = utility.dataForOne(symbol, "percent_change_24h")
    #         st.bar_chart(perChange24hdf)

    #         st.header("Market Dominance")
    #         marketdominancedf = utility.dataForOne(symbol, "market_dominance")
    #         st.line_chart(marketdominancedf)

    # with st.expander("Analyse"):

    symbols = st.multiselect("Select Coin(s)", utility.symbols[:3000])

    # col1, col2 = st.columns((1,1))

    # col1.header(f'{symbols[0]}')
    # col1.subheader(f'')
    # col2.header(f'price  percentageChange')


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