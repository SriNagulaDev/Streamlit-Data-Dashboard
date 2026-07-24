import streamlit as st
import pandas as pd

st.title("My Dashboard")
st.write("Welcome to my Streamlit dashboard!, This is beginning of something cool.")

st.subheader("Sentimental Analysis of tweets, about US Airlines.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Here's a preview of your data:")
    st.dataframe(df)