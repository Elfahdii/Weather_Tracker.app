import streamlit as st
import pandas as pd
import random
st.title("Predict Tomorrow's Weather")

df = pd.read_csv("weather_data.csv")

if st.button("Predict"):
    conditions = df["Condition"].tolist()
    prediction = random.choice(conditions)

    st.write("Based on past observations, tomorrow might be:", prediction)