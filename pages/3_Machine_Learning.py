import streamlit as st
from PIL import Image
image1 = Image.open('images/blood.PNG')
image2 = Image.open('images/recipe.PNG')
image3 = Image.open('images/credit.PNG')
image4 = Image.open('images/llm.gif')

st.set_page_config(layout="wide")
st.header("Machine Learning")
st.write("Listed below are the Machine Learning projects I have worked on.")

st.divider()

#expander = st.expander(expanded=True)

with st.expander(':blue[**1. Social Media Post Analytics**]', expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
**:green[Problem Description:]** The goal was to leverage the power of Large Language Models for producing brief summaries and sentiments of the comment section of the Linkedin post.
\n**:green[Problem Type:]** Deep Learning, Generative AI, MLOps
\n**:green[Solution:]** Using BART-based model for summarization and RoBERTa-based model for sentiment analysis, built a web application that allows user to select a post to return a dashboard with sentiment plot, summary table, and word cloud.
\n**:green[Impact:]** Once deployed, the app can help Linkedin influencers to have a quick analysis of their content.
''')
    with col2:
        st.image(image4)
    st.markdown('''
**:green[Tools & Technology:]** Transformers, HuggingFace, Streamlit, Python, LLMs
''')

with st.expander(':blue[**2. Blood Donation Prediction**]', expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
**:green[Problem Description:]** The dataset owners are interested in predicting if past blood donors will donate again during the next collection date as part of an effort to forecast blood supply to mitigate potential supply shortages.
\n**:green[Problem Type:]** Supervised Learning, Binary Classification
\n**:green[Solution:]** By performing in-depth data cleaning and training and testing several classifiers, including Logistic Regression and K-Nearest Neighbors with Repeated Stratified K-Fold cross-validation, I produced a model that outperforms the ZeroR baseline accuracy by 5.3%.
\n**:green[Impact:]** This model offers the Blood Transfusion Service Center in Hsin-Chu City in Taiwan a more realistic estimate of the number of donors to expect, allowing them to derive a more accurate forecasting of future blood supply and take appropriate action to address potential shortages.
''')
    with col2:
        st.image(image1)
    st.markdown('''
**:green[Tools & Technology:]** Python, Scikit-Learn, Jupyter Notebook
\n[**:blue[Click here to see the work]**](https://github.com/mahipal-z/Blood-donation-project/blob/main/BloodTransfusion.ipynb)
''')

with st.expander(':blue[**3. Rating Prediction for a Recipe Website**]', expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
**:green[Problem Description:]** An online recipe start-up owners wanted to increase website traffic by publishing recipes that are likely to receive high user ratings. To do so, they want to avoid publishing recipes with potentially low ratings. They wanted to know if it is possible to detect recipe ratings using past data.
\n**:green[Problem Type:]** Binary Classification, Natural Language Processing
\n**:green[Solution:]** Using NLP techniques to extract features from recipes' text, dimensionality reduction to distil the features, oversampling to balance the dataset, and hyperparameter tuning to identify the best hyperparameters, I developed an XGBoost classification model with an 18% higher recall value than the client's expectations. Based on this model, I identified and provided the client with recommendations to increase website traffic.
    ''')
    with col2:
        st.image(image2)
    st.markdown('''
**:green[Impact:]** The model can help strategize future content publication, forecast user ratings, and increase website traffic.
\n**:green[Tools & Technology:]** Jupyter Notebooks, Pandas, nltk library, Scikit-learn
\n[**:blue[Click here to see the work]**](https://github.com/mahipal-z/Recipe-Rating-Prediction/blob/main/notebook.ipynb)
''')

with st.expander(':blue[**4. Predicting Credit Card Approvals**]', expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('''
**:green[Problem Description:]** The project's objective was to reduce the time and cost of the credit card application screening process. This cost reduction will allow banking clients to offer online financial advising services for free to new customers opting for an upgraded credit card account.
\n**:green[Problem Type:]** Binary Classification, Financial Analysis, Risk Analysis
\n**:green[Solution:]** After one-hot encoding, and mean imputation on the dataset, I developed a Logistic Regression model achieving the target classification accuracy using MinMaxScaler and Grid Search cross validation and Found insights that can help provide financial advice to customers for building high credit score.
\n**:green[Impact:]** The model automates the initial screening process of credit card applications, saving banks time and resources.
\n**:green[Tools & Technology:]** Jupyter Notebooks, Pandas, Numpy, Scikit-learn
''')
    with col2:
        st.image(image3)
    st.markdown('''
[**:blue[Click here to see the work]**](https://github.com/mahipal-z/Credit-card-approval-prediction/blob/main/notebook.ipynb)
''')

with st.expander(':blue[**5. Performance prediction of Laboratory equipment**]', expanded=True):
    st.markdown('''
**:green[Problem Description:]** Fluid mechanics lab costs much time and capital in running the same experiments several times during a semester for educational purposes. We wanted to develop a tool that can predict the performance of centrifugal blower, a lab equipment, accurately to avoid performing actual experiments on it.
\n**:green[Problem Type:]** Supervised Learning, Linear Regression
\n**:green[Solution:]** Collected the past experimental data for the equipment and performed some experiments using combinations of different variables. Trained a regression model using a neural network tool and achieved 0.92 of coefficient of determination (R squared).
\n**:green[Impact:]** The tool improved the teaching process and learning experience by providing the flexibility to perform experiments in class when Laboratory is unavailable.
\n**:green[Tools & Technology:]** Visual Gene Developer, Neural Networks
''')
