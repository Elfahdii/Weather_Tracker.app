import streamlit as st
import pandas as pd
import math


df = pd.read_csv("weather_data.csv")



if st.button("View"):
   if not df.empty:

    average_temp = df["Temperature"].mean()
    min_temp = df["Temperature"].min()
    max_temp = df["Temperature"].max()
    common_condition = df["Condition"].mode()[0]

    st.write("Average temperature:", math.ceil(average_temp))
    st.write("Minimum temperature:", min_temp)
    st.write("Maximum temperature:", max_temp)
    st.write("Most common condition:", common_condition)

else:
    st.warning("No weather observations found yet.")


    