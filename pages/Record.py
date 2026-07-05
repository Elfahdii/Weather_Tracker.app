import streamlit as st
import datetime
import csv 
import os


date = st.date_input("Enter the date", datetime.date(2026, 5, 7))
temperature = st.number_input("Enter the Temperature", 0)
condition = st.selectbox("What's today's weather?", ("sunny", "rainy", "cloudy"))
humidity = st.number_input("Enter the humidity percentage", 0)
speed = st.number_input("Enter the speed in km", 0)


if st.button("Submit"):
    file_exists = os.path.isfile("weather_data.csv")

    with open("weather_data.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Date", "Temperature", "Condition", "Humidity", "Wind Speed"])

        writer.writerow([date, temperature, condition, humidity, speed])

    st.success("Weather observation saved!")