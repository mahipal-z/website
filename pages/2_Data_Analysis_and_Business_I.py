import streamlit as st
import pandas as pd

st.title("Data Analysis and Business Intelligence")

df1 = pd.read_excel("DA.xlsx", header=None, names=None)

st.dataframe(data=df1)

