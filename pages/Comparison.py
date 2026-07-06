import streamlit as st
import pandas as pd


st.title("Compare This Year vs Last Year")

df = pd.read_csv("weather_data.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year

this_year = st.number_input("Enter this year", value=2026)
last_year = this_year - 1

this_year_data = df[df["Year"] == this_year]
last_year_data = df[df["Year"] == last_year]

if st.button("Compare"):
    st.subheader(f"{this_year} Weather")
    st.write("Average temperature:", round(this_year_data["Temperature"].mean(), 2))
    st.write("Minimum temperature:", this_year_data["Temperature"].min())
    st.write("Maximum temperature:", this_year_data["Temperature"].max())

    st.subheader(f"{last_year} Weather")
    st.write("Average temperature:", round(last_year_data["Temperature"].mean(), 2))
    st.write("Minimum temperature:", last_year_data["Temperature"].min())
    st.write("Maximum temperature:", last_year_data["Temperature"].max())