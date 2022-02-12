import streamlit as st
from pages import utility

def app():
    with st.expander("Analyse Currency"):
        symbol = st.selectbox("Select Coin", utility.symbols[:3000])
        if symbol:
            col1,col2 = st.columns(2)
            # Timeframe =col1.multiselect("Timeframe", ["1D", "1W", "1M", "3M", "6M", "1Y"])
            df = utility.lunarData(symbol)
            st.dataframe(df)


            st.write("Price")
            closedf = utility.dataForOne(symbol, "close")
            st.area_chart(closedf)

            st.write("Volume")
            volumedf = utility.dataForOne(symbol, "volume")
            st.bar_chart(volumedf)

            st.write("Volatility")
            volatilitydf = utility.dataForOne(symbol, "volatility")
            st.line_chart(volatilitydf)

            st.write("Percent Change 24h")
            perChange24hdf = utility.dataForOne(symbol, "percent_change_24h")
            st.bar_chart(perChange24hdf)

            st.write("Market Dominance")
            marketdominancedf = utility.dataForOne(symbol, "market_dominance")
            st.line_chart(marketdominancedf)

    with st.expander("Compare multiple Currencies"):
        symbol = st.multiselect("Select Coin(s)", utility.symbols[:3000])
        if len(symbol) == 2:
            
            st.write("Price")
            closedf = utility.compBtwTwoCoinsBasesAttribute(symbol[0], symbol[1], "close")
            st.area_chart(closedf)

            st.write("Volume")
            volumedf = utility.compBtwTwoCoinsBasesAttribute(symbol[0], symbol[1], "volume")
            st.bar_chart(volumedf)

            st.write("Volatility")
            volatilitydf = utility.compBtwTwoCoinsBasesAttribute(symbol[0], symbol[1], "volatility")
            st.line_chart(volatilitydf)

            st.write("Percent Change 24h")
            perChange24hdf = utility.compBtwTwoCoinsBasesAttribute(symbol[0], symbol[1], "percent_change_24h")
            st.bar_chart(perChange24hdf)

            st.write("Market Dominance")
            marketdominancedf = utility.compBtwTwoCoinsBasesAttribute(symbol[0], symbol[1], "market_dominance")
            st.line_chart(marketdominancedf)
            # df = utility.percChangeBtwTwo(symbol[0], symbol[1])
            # st.line_chart(df)



    

# col2.write("test")
# make comparison graph for selected currencies
# i.e. percentage change in price everyday
# if you want to limit comparison between 2 coins
# make graph for comparison between 2 coins