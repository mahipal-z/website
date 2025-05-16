import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

image1 = Image.open('images/Photo Web.jpg')
image2 = Image.open('images/profile.jpg')

image3 = Image.open('images/data_scientist_professional_badge.png')
image4 = Image.open('images/snowflakeDE1.png')
image5 = Image.open('images/snowflakeDW2.png')
image6 = Image.open('images/aws-certified-database-specialty.png')
image7 = Image.open('images/aws-certified-data-analytics-specialty.png')
image8 = Image.open('images/aws-certified-developer-associate.png')
image9 = Image.open('images/aws-certified-machine-learning-specialty.png')
image10 = Image.open('images/uottawa.png')
image11 = Image.open('images/stanford.png')
image12 = Image.open('images/dc.PNG')

st.set_page_config( 
    page_title="Mahipal Zanakat",
    page_icon=image2 
)

st.markdown("""
<style>
.big-font {
    font-size:25px !important;
}
</style>
""", unsafe_allow_html=True)




######################
#main page layout
######################

col1, col2 = st.columns([0.7, 0.3], gap="large")

with col1:
    st.title("About Me")
    st.markdown(
  """Everyday engineer who possesses a strong interest in everything data :bar_chart:, cloud :cloud:, and emerging technologies :robot_face:.
  Someone who will enjoy being part of your Data/Analytics/AI team. """)

    st.markdown("""Currently invested in
    \n- Investigating EMR systems
    \n- Finding insights and building dashboards
    \n- Pushing for data literacy, data democratization and data quality initiatives
    \n- at the largest health authority in British Columbia
     """)
    st.markdown("""\n""")
    st.markdown("""**Connect with me on** [**LinkedIn**](https://www.linkedin.com/in/mahipalzanakat) | [**GitHub**](https://github.com/mahipal-z) | [**Medium**](https://medium.com/@storiesbymahipal)
  """)
    
with col2:
    st.markdown('<p class="big-font">Mahipal Zanakat</p>', unsafe_allow_html=True)
    st.image(image1, width=200)

st.divider()

st.subheader('Tech Blogs')

st.markdown("""[**Data Lake For Dummies**](https://medium.com/data-dynamics-and-cloud-navigation/data-lake-for-dummies-7f593a83f249) 
\n[**How to build an EL[T] pipeline using Singer taps and Meltano CLI**](https://medium.com/@storiesbymahipal/how-to-build-an-el-t-pipeline-using-singer-taps-and-meltano-cli-84a8b519a4c0) 
\n[**How to query S3 data in dbt using Redshift Spectrum**](https://medium.com/@storiesbymahipal/how-to-query-s3-data-in-dbt-using-redshift-spectrum-3188b7e7a684)
\n[**Querying a machine learning model for Insights**](https://www.linkedin.com/pulse/querying-machine-learning-model-insights-mahipal-zanakat/)
  """)

st.divider()

st.subheader('I could be a good company if')
st.markdown("""
You challenge me to a game of Chess :chess_pawn: [@chess.com](https://friend.chess.com/W7Xra)
\nor Hiking :runner: nearby or trying a new restaurant :shallow_pan_of_food:
\nor Bowling :bowling:, Lifting Weights :weight_lifter:, Card games, Board games :game_die:, or for Cooking
\nor you are willing to teach me Swimming :swimmer:, Pool :8ball:, or Piano :musical_keyboard:
""")
#    st.markdown()

st.divider()

st.subheader("Certification")
st.image([image3,image4,image5], width=200)
st.image([image6,image7,image8,image9], width=170)
st.markdown("""**Validation Credentials** [**Credly**](https://www.credly.com/users/mahipal-zanakat) | [**DataCamp**](https://www.datacamp.com/certificate/DS0021765360075)""")

#components.html("""<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="8e92d3b3-1cfa-4ad3-8173-a4c06bb239a2" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>"""
#                ,height=250)
st.divider()
st.subheader("Alma Mater")
col3, col4, col5 = st.columns(3)

with col3:
    st.image(image10, width=150)
    st.markdown("""**Master of Engineering, Mechanical**""")
        
with col4:
    st.image(image12, width=150)
    st.markdown("""**Data Scientist in Python**""")
    st.markdown("""**Data Analyst in SQL**""")

with col5:
    st.image(image11, width=150)
    st.markdown("""**Machine Learning by Andrew Ng.**""")
    
######################
#sidebar layout
######################

#st.sidebar.subheader("Portfolio")

            
