import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns
sns.set()


data=pd.read_csv("CAPSTONEDATA.csv")
st.write("Sales Daily Chart")
st.line_chart(data,x="PROJDATE", y="NETSALES")

st.markdown(
    """<hr style="border-top:1px solid white; width:100%">""",
    unsafe_allow_html=True
)

st.write("Net Sales histogram")
fig, ax=plt.subplots()
plt.hist(data["NETSALES"],bins=10)
st.pyplot(fig)

st.markdown(
    """<hr style="border-top:1px solid white; width:100%">""",
    unsafe_allow_html=True
)


