import streamlit as st
from PIL import Image
image1 = Image.open('images/blood.PNG')
image2 = Image.open('images/recipe.PNG')
image3 = Image.open('images/credit.PNG')
#image4 = Image.open('images/playstore.PNG')

st.set_page_config(layout="wide")
st.header("Data Engineering")
st.write("Listed below are the Data Engineerining projects I have worked on.")

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

with st.expander(':blue[**2. •	Accelerating vaccine development using AI Engineering**]', expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
**:green[Problem Description:]** To develop a vaccine for a deadly disease caused by the John-Cunningham virus, prediction of the best protein candidates was needed, resulting in a ranking system for the antigens. The client needed an analysis tool to compare and rank antigens, collect relevant data sets, and ensure the validity and accuracy of the AI model.
\n**:green[Problem Type:]** Extract, Transform and Load, Data Collection, MLOps
\n**:green[Solution:]** Automated the ETL pipeline to gather data from various Bioinformatics tools and provide a clean dataset, developed a ranking mechanism for protein candidates and deployed the analytics application in the end.
\n**:green[Impact:]** The project reduced the time required in months for clinical trials by providing insights from publicly available research. 
''')
    with col2:
        st.image(image1)
    st.markdown('''
**:green[Tools & Technology:]** Selenium, Web Scrapping, API integration, Machine learning, Streamlit
\n[**:blue[Click here for certificate of recognition]**](https://www.linkedin.com/posts/activity-7063171186083467264-xjIg/?utm_source=share&utm_medium=member_desktop)
''')
