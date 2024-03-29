import streamlit as st
from PIL import Image
image1 = Image.open('images/datalake.PNG')
#image2 = Image.open('images/farm_params.jpg')
image3 = Image.open('images/belyntic.PNG')
image4 = Image.open('images/optimized-web-app.gif')
image5 = Image.open('images/iryss_roadmap.PNG')

st.set_page_config(layout="wide")
st.header("Data Engineering and MLOps")
st.write("Listed below are the Data Engineerining and MLOps projects I have worked on.")

st.divider()

#expander = st.expander(expanded=True)

with st.expander(':blue[**1. Implementation of data lake design using AWS CloudFormation**]', expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
**:green[Problem Description:]** The aim was to create the data lake architecture, where the raw data is copied over to an S3 bucket from a source bucket by a lambda function, combined by an AWS Glue job, and finally transformed by another AWS Glue job to parquet format and stored in the final S3 bucket.
\n**:green[Problem Type:]** Extract, Transform and Load, Pipeline Automation
\n**:green[Solution:]** Developed an AWS CloudFormation template, Lambda code, and Glue job scripts. Deployed the Stack on the cloud and configured the ETL pipeline using S3 Event notification.
''')
    with col2:
        st.image(image1)
    st.markdown('''
**:green[Tools & Technology:]** AWS, CloudFormation, S3, Lambda, Glue, Python, Apache Spark, Infrastructure as Code
\n[**:blue[Click here for Blog Post]**](https://medium.com/data-dynamics-and-cloud-navigation/data-lake-for-dummies-7f593a83f249)
''')

with st.expander(':blue[**2. Farm Yield Analytics**]', expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
**:green[Problem Description:]** The aim was to look through the data provided by a large farming company to make predictions and provide recommendations that help them make more money.
\n**:green[Problem Type:]** Data Analytics, MLOps
\n**:green[Solution:]** Leveraged the dataset to build a Machine Learning application that generates plots to optimize farming parameters, predicts yield for the set farming conditions and provide model explanation.
''')
    with col2:
        st.image(image4)
    st.markdown('''
**:green[Tools & Technology:]** Python, Pandas, Scikit-learn, Streamlit
\n[**:blue[Click here to see Web Application]**](https://mahipal-z-farm-yield-analytics-streamlit-l00xze.streamlit.app/)
''')

with st.expander(':blue[**3. Accelerating vaccine development using AI Engineering**]', expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
**:green[Problem Description:]** To develop a vaccine for a deadly disease caused by the John-Cunningham virus, prediction of the best protein candidates was needed, resulting in a ranking system for the antigens. The client needed an analysis tool to compare and rank antigens, collect relevant data sets, and ensure the validity and accuracy of the AI model.
\n**:green[Problem Type:]** Extract, Transform and Load, Data Collection, MLOps
\n**:green[Solution:]** Automated the ETL pipeline to gather data from various bioinformatics tools and provided a clean dataset. Developed a ranking mechanism for protein candidates and deployed the analytics application in the end.
''')
    with col2:
        st.image(image3)
    st.markdown('''
**:green[Impact:]** The project reduced the time required for clinical trials by months by providing the solution to identify the most promising proteins for developing the vaccine.
\n**:green[Tools & Technology:]** Selenium, Web Scrapping, API integration, Machine learning, Streamlit
\n[**:blue[Click here for Certificate of recognition]**](https://www.linkedin.com/posts/activity-7063171186083467264-xjIg/?utm_source=share&utm_medium=member_desktop)
''')

with st.expander(':blue[**4. Forecasting Out-of-Pocket Treatment Cost for Lung Cancer Patients in United States**]', expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
**:green[Problem Description:]** To provide financial guide for Lung Cancer patients at the time of the diagnosis, client required a machine learning solution that can estimate the annual out-of-pocket cost for entire treatment.
\n**:green[Problem Type:]** Data Collection, Data Validation, Supervised Learning, MLOps
\n**:green[Solution:]** Cleaned, transformed and validated data, built a dashboard to deliver insights and analytics, trained the XGBregressor model to predict the cost and dockerized web application for the client to deploy on premises.
''')
    with col2:
        st.image(image5)
    st.markdown('''
**:green[Impact:]** Over 40% of patients with stage 3&4 lung cancer declare personal bankruptcy within 4 years of diagnosis. This solution will serve as a financial guide for those people.
\n**:green[Tools & Technology:]** MLFlow, Streamlit, Docker, Python
''')
