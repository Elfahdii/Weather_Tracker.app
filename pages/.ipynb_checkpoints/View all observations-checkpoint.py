import streamlit as st
import pandas as pd

st.title("All Weather Observations")

df = pd.read_csv("weather_data.csv")

if st.button("View All Observations"):
    st.dataframe(df)