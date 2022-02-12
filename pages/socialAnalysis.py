import streamlit as st
from pages import utility
import json
import pandas as pd 

def app():
    symbol = st.selectbox("Coin", utility.symbols[:3000])
    df = utility.lunarData(symbol)
    st.dataframe(df)
    # st.json(data)
    with st.expander("Twitter"):
        st.line_chart(df[['tweets','tweet_spam']])

        influencers = utility.socialData(symbol)
        st.json(influencers)

    with st.expander("reddit"):
        st.write("reddit")
    
    
    
    

    # twitter_df = pd[['tweets', 'tweet_spam', 'tweet_followers', 'tweet_quotes', 'tweet_retweets', 'tweet_replies', 'tweet_favourites', 'tweet_sentiment1', 'tweet_sentiment_impact1']]
    
    # reddit_df = pd[['reddit_posts', 'reddit_post_score', 'reddit_comments','reddit_comments_score' ]]
    
    # otherData_df = pd[['social_dominance_calc_24h_previous',
    #                    'social_contributors_calc_24h_previous',
    #                    'url_shares_calc_24h_previous',
    #                    'tweet_spam_calc_24h_previous',
    #                    'news_calc_24h_previous',
    #                    'average_sentiment_calc_24h_previous',
    #                    'social_score_calc_24h_previous',
    #                    'social_contributors_calc_24h',
    #                    'social_contributors_calc_24h_percent',
    #                    'url_shares_calc_24h',
    #                    'url_shares_calc_24h_percent',
    #                    'news_calc_24h',
    #                    'average_sentiment_calc_24h',
    #                    'social_score_calc_24h',
    #                    'social_score_calc_24h_percent',
    #                    'social_volume_calc_24h',
    #                    'social_volume_calc_24h_percent']]

    # 365 days historical data