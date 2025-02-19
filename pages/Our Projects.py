import streamlit as st
import pandas as pd

st.title("Data Table")

data= pd.read_csv("CAPSTONEDATA.csv")
df = pd.DataFrame(data)
selected_column = df[['COUNTRY','PROFITAFTERTAX','CSAT']]
st.table(selected_column)