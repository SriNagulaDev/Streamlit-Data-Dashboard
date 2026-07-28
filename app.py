import streamlit as st
import pandas as pd

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