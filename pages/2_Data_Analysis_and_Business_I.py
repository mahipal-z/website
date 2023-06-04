import streamlit as st
import pandas as pd

st.title("Data Analysis and Business Intelligence")

df1 = pd.read_excel("DA.xlsx", header=None, names=None)

st.dataframe(data=df1, height=1000, use_container_width=True, hide_index=True, column_config=None)

