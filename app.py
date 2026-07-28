import streamlit as st
import pandas as pd
import plotly.express as px

st.title("My Dashboard")
st.write("Welcome to my Streamlit dashboard!, This is beginning of something cool.")

st.subheader("Sentimental Analysis of tweets, about US Airlines.")
st.markdown("This dashboard allows you to analyze the sentiment of tweets related to US Airlines. You can upload your own CSV file containing tweet data and visualize the sentiment analysis results.🐦")

st.sidebar.title("Navigation")
st.sidebar.markdown("This dashboard allows you to analyze the sentiment of tweets related to US Airlines. You can upload your own CSV file containing tweet data and visualize the sentiment analysis results.🐦")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.write("Here's a preview of your data:")
    st.dataframe(df)

    st.sidebar.subheader("Show random tweets")
    random_tweet = st.sidebar.radio('Sentiment', ('positive', 'neutral', 'negative'))
    st.sidebar.markdown(df.query('airline_sentiment == @random_tweet')[['text']].sample(n=1).iat[0, 0])

    st.subheader("Tweet Sentiment Count")
    sentiment_count = df['airline_sentiment'].value_counts()
    sentiment_df = pd.DataFrame({
        'Sentiment': sentiment_count.index,
        'Tweets': sentiment_count.values
    })

    fig = px.bar(sentiment_df, x='Sentiment', y='Tweets', color='Sentiment')
    st.plotly_chart(fig)

    airline_count = df['airline'].value_counts()
    airline_df = pd.DataFrame({
        'Airline': airline_count.index,
        'Tweets': airline_count.values
    })

    st.subheader("Tweets by Airline")
    airline_fig = px.bar(airline_df, x='Airline', y='Tweets', color='Airline')
    st.plotly_chart(airline_fig)
















