import streamlit as st
from pages import utility
import streamlit.components.v1 as components
# import json
# import pandas as pd 

def app():
    st.header("Social Analysis")
    symbol = st.multiselect("Select The Coin(s)", utility.symbols[:3000])
    if len(symbol) == 1:
        df = utility.lunarData(symbol)
        st.dataframe(df)

        # st.json(data)

        influencers = utility.socialData(symbol)
    
        with st.expander("Twitter"):

            st.header("Number Of Bullish vs Bearish Post")
            bvb = utility.bullvsbear(symbol)
            st.bar_chart(bvb)

            st.header("tweet")
            tweetdf = utility.dataForOne(symbol,"tweets")
            st.line_chart(tweetdf)

            st.header("perChange Tweets vs perChange price")
            pctdf = utility.perChange(symbol, 'tweets')
            st.line_chart(pctdf)

            st.header("tweet_spam")
            tweetSpamdf = utility.dataForOne(symbol,"tweet_spam")
            st.line_chart(tweetSpamdf)

            st.header("tweet_followers")
            tweetFollowersdf = utility.dataForOne(symbol,"tweet_followers")
            st.bar_chart(tweetFollowersdf)

            st.header("perChange TweetFollowers vs perChange price")
            testdf1 = utility.perChange(symbol, 'tweet_followers')
            st.line_chart(testdf1)

            st.header("tweet_retweets")
            tweetRetweetsdf = utility.dataForOne(symbol,"tweet_retweets")
            st.area_chart(tweetRetweetsdf)

            st.header("perChange TweetFollowers vs perChange price")
            testdf2 = utility.perChange(symbol, 'tweet_retweets')
            st.line_chart(testdf2)
            
            # resS = utility.feeds(symbol[0])
            # for res in resS:
            #     components.html(res,height= 700)    

            # st.json(influencers)

        with st.expander("reddit"):
            st.header("Reddit Posts")
            redditPostsdf = utility.dataForOne(symbol,"reddit_posts")
            st.line_chart(redditPostsdf)

            st.header("perChange RedditPosts vs perChange price")
            testdf3 = utility.perChange(symbol, 'reddit_posts')
            st.line_chart(testdf3)

            st.header("Reddit Posts Scores")
            redditPostsScoredf = utility.dataForOne(symbol,"reddit_posts_score")
            st.line_chart(redditPostsScoredf)

            st.header("perChange RedditPostsScore vs perChange price")
            testdf4 = utility.perChange(symbol, 'reddit_posts_score')
            st.line_chart(testdf4)

# with st.expander("Compare"):
#     symbols = st.multiselect("Select Coins", utility.symbols[:3000])
    if len(symbol)>1:
        SICdf = utility.compMultiCryptoBasesAttr(symbol, 'social_impact_score')
        st.line_chart(SICdf)

        st.header("tweet")
        tweetdf = utility.compMultiCryptoBasesAttr(symbol, "tweets")
        st.bar_chart(tweetdf)

        st.header("tweet_spam")
        tweetSpamdf = utility.compMultiCryptoBasesAttr(symbol,"tweet_spam")
        st.bar_chart(tweetSpamdf)

        st.header("tweet_followers")
        tweetFollowersdf = utility.compMultiCryptoBasesAttr(symbol, "tweet_followers")
        st.line_chart(tweetFollowersdf)

        st.header("tweet_retweets")
        tweetRetweetsdf = utility.compMultiCryptoBasesAttr(symbol, "tweet_retweets")
        st.area_chart(tweetRetweetsdf)




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