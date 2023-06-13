

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
  """Everyday engineer who possess strong interest in everything data :bar_chart:, cloud :cloud:, and emerging technologies :robot_face:.
  Someone who will enjoy being part of your Data/AI/ML team. """)

    st.markdown("""Currently invested in
    \n Designing and integrating ETL/ELT pipelines
    \n Collecting and cleaning data 
    \n Finding insights and building dashboards
    \n Developing and deploying ML models
     """)
    st.markdown("""\n""")
    st.markdown("""**Connect with me on** [**LinkedIn**](https://www.linkedin.com/in/mahipalzanakat) | [**GitHub**](https://github.com/mahipal-z) | [**Medium**](https://medium.com/@storiesbymahipal)
  """)
    
with col2:
    st.markdown('<p class="big-font">Mahipal Zanakat</p>', unsafe_allow_html=True)
    st.image(image1, width=200)

st.divider()


st.subheader("I could be a good company if")
st.markdown("""
You challenge me to a game of Chess :chess_pawn: [@chess.com](https://friend.chess.com/W7Xra)
\nor Hiking :runner: nearby or trying a new restaurant :shallow_pan_of_food:
\nor Bowling :bowling:, Lifting Weights :weight_lifter:, Card games, Board games :game_die:, or for Cooking
\nor you are willing to teach me Swimming :swimmer:, Golfing :golfer:, Pool :8ball:, or Piano :musical_keyboard:
"""
)

st.divider()

st.subheader("Certification")
st.image([image3,image4,image5], width=200)

st.image([image6,image7,image8,image9], width=170)

st.markdown("""**Validation Credentials** [**Credly**](https://www.credly.com/users/mahipal-zanakat) | [**DataCamp**](https://www.datacamp.com/certificate/DS0021765360075)""")

#components.html("""<div data-iframe-width="150" data-iframe-height="270" data-share-badge-id="8e92d3b3-1cfa-4ad3-8173-a4c06bb239a2" data-share-badge-host="https://www.credly.com"></div><script type="text/javascript" async src="//cdn.credly.com/assets/utilities/embed.js"></script>"""
#                ,height=250)
st.divider()
st.subheader("Education")

st.markdown("""**Master of Engineering, Mechanical | University of Ottawa**
         \n**Data Scientist in Python | DataCamp**
         \n**Data Analyst in SQL | DataCamp**
         \n**Machine Learning by Andrew Ng. | Stanford University**""")

#with col2:
    
######################
#sidebar layout
######################

st.sidebar.subheader("Portfolio")

            
