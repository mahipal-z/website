import streamlit as st

st.title("Data Analysis and Business Intelligence")

st.divider()

st.header(':blue[1. Exploratory data analysis of the top 400 video games released since 1977]')
st.markdown('''
**:green[Problem Description:]** The objective was to do a market research analysis of video games sector by identifying release years that users and critics liked best and exploring the business side of gaming by looking at game sales data.
\n**:green[Problem Type:]** Exploratory Data Analysis (EDA)
\n**:green[Solution:]** Compared the sales dataset with the critic and user reviews to determine whether video games have improved as the gaming market has grown. Found answers to several business questions using joins, set theory, grouping, filtering, and ordering techniques.
\n**:green[Impact:]** The findings from this analysis provides insights to developer team that helps them finalize the Game Design Document during the pre-production stage.
\n**:green[Tools & Technology:]** Relational databases, PostgreSQL
\n[**:blue[Click here to see analysis]**](https://github.com/mahipal-z/Videogames-EDA/blob/main/notebook.ipynb)
''')









#####################################################################################################
#import pandas as pd
#df1 = pd.read_excel("DA.xlsx", header=None, names=None)

#st.dataframe(data=df1, height=1000, use_container_width=True, hide_index=True, column_config=None)

