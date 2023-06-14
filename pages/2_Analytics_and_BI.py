import streamlit as st
from PIL import Image
image1 = Image.open('images/videogames.jpg')
image2 = Image.open('images/powerbi.PNG')
image3 = Image.open('images/tableau.PNG')
image4 = Image.open('images/playstore.PNG')
#image5 = Image.open('images/')

st.set_page_config(layout="wide")
st.header("Data Analysis and Business Intelligence")
st.write("Listed below are the data analytics projects I have worked on.")

st.divider()

#expander = st.expander(expanded=True)

with st.expander(':blue[**1. Exploratory data analysis of the top 400 video games**]', expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
**:green[Problem Description:]** The objective was to do a market research analysis of video games sector by identifying release years that users and critics liked best and exploring the business side of gaming by looking at game sales data.
\n**:green[Problem Type:]** Exploratory Data Analysis (EDA)
\n**:green[Solution:]** Compared the sales dataset with the critic and user reviews to determine whether video games have improved as the gaming market has grown. Found answers to several business questions using joins, set theory, grouping, filtering, and ordering techniques.
''')
    with col2:
        st.image(image1,width=500)
    st.markdown('''
**:green[Impact:]** The findings from this analysis provides insights to the developer team that helps them finalize the Game Design Document during the pre-production stage.
\n**:green[Tools & Technology:]** Relational databases, PostgreSQL
\n[**:blue[Click here to see analysis]**](https://github.com/mahipal-z/Videogames-EDA/blob/main/notebook.ipynb)
''')

with st.expander(':blue[**2. Identifying key factors influencing heart disease using PowerBI**]', expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
**:green[Problem Description:]** Project’s goal was to build an interactive dashboard from the dataset of patients with heart disease and investigate what factors impact the most in the diagnosis of heart disease.
\n**:green[Problem Type:]** Dashboard and Reporting
\n**:green[Solution:]** Developed a live visual report which displays the relationship between the likelihood of having a heart disease with factors such as age, gender, lifestyle, etc. using slicers, bar plots, and filters by integrating a Kaggle dataset into Microsoft PowerBI.
''')
    with col2:
        st.image(image2)
    st.markdown('''
**:green[Impact:]** The dashboard provides a quick overview of findings from the data set and the accessibility to dig deeper into each section of the analysis.
\n**:green[Tools & Technology:]** PowerBI, Relational Databases
\n[**:blue[Click here for PowerBI Dashboard]**](https://www.youtube.com/watch?v=sMiuQQ0Qyz0&ab_channel=MahipalZanakat)
''')

with st.expander(':blue[**3. Retail store KPI Dashboard**]', expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
**:green[Problem Description:]** The goal was to analyze the dataset containing information related to Sales, Profits, and other interesting facts about a superstore giant and publish a dashboard.
\n**:green[Problem Type:]** Dashboard and Reporting
\n**:green[Solution:]** Validated the dataset, integrated with Tableau, analyzed data in worksheets, and summarised using an overview dashboard.
\n**:green[Impact:]** The report provides a sneak peek of sales and profit numbers in different regions of the United States with a filtering ability to categorize and group data.
\n**:green[Tools & Technology:]** Tableau, Data Engineering, Data Analysis
''')
    with col2:
        st.image(image3)
    st.markdown('''
[**:blue[Click here for KPI Dashboard]**](https://public.tableau.com/app/profile/mahipal.zanakat/viz/RetailStoreKPIDashboard/RetailStoreKPIDashboard)
''')

with st.expander(':blue[**4. Comprehensive analysis of the android app market by comparing over 10,000 apps in Play Store**]', expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
**:green[Problem Description:]** The objective was to look for insights in the data to devise strategies to drive growth and retention.
\n**:green[Problem Type:]** Data Analysis and Visualization, Sentiment Analysis
\n**:green[Solution:]** I did the exploratory data analysis to answer important business questions on app categories, size, and pricing on Google Play Store. Cleaned and merged tables to explore the user ratings and plotted sentiment polarity score.
\n**:green[Impact:]** The findings from this analysis can help decide what type of apps to develop, how much it should be priced and identify what makes users happy.
\n**:green[Tools & Technology:]** Relational databases, Python, Pandas, Plotly
''')
    with col2:
        st.image(image4)
    st.markdown('''
[**:blue[Click here to see analysis]**](https://github.com/mahipal-z/playstore-apps-eda/blob/main/Android%20App%20Market%20EDA.ipynb)
''')


with st.expander(':blue[**5. Simulation of Airport Check-in System**]', expanded=True):
    st.markdown('''
**:green[Problem Description:]** The goal was to measure the effect of various factors on the real-time performance of an airport’s check-in operations. Additionally, management wanted to have a strategy that can minimize the cost of the operations without hurting the customer satisfaction score.
\n**:green[Problem Type:]** Data Visualization, System Engineering, Operation Research
\n**:green[Solution:]** Using data collected for a week, I built and executed a model in a simulation software that can report a real-time percentage of passengers satisfied/dissatisfied by using the airport check-in service. Also, provided an experimenter tool that provides resource allocation solution that improved customer service with minimum cost.
\n**:green[Impact:]** For the given business case, the model can save CAD 190,000 in opportunity cost and CAD 255,000 in operations cost.
\n**:green[Tools & Technology:]** Witness Horizon, Witness Action Language
''')







#####################################################################################################
#import pandas as pd
#df1 = pd.read_excel("DA.xlsx", header=None, names=None)

#st.dataframe(data=df1, height=1000, use_container_width=True, hide_index=True, column_config=None)

