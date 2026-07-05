import streamlit as st
import pandas as pd

st.title("Search Observations by Date")

search_date = st.date_input("Choose a date")

df = pd.read_csv("weather_data.csv")

if st.button("Search"):
    result = df[df["Date"] == str(search_date)]

    if not result.empty:
        st.write("Observations from this date:")
        st.dataframe(result)
    else:
        st.warning("No observations found for this date.")