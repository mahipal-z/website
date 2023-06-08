

import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

image1 = Image.open('Photo Web.jpg')
image2 = Image.open('profile.jpg')

image3 = Image.open('data_scientist_professional_badge.png')
image4 = Image.open('snowflakeDE1.png')
image5 = Image.open('snowflakeDW2.png')
image6 = Image.open('aws-certified-database-specialty.png')
image7 = Image.open('aws-certified-data-analytics-specialty.png')
image8 = Image.open('aws-certified-developer-associate.png')
image9 = Image.open('aws-certified-machine-learning-specialty.png')

st.set_page_config( 
    page_title="Mahipal Zanakat",
    page_icon=image2 
)


######################
#main page layout
######################

col1, col2 = st.columns([0.7, 0.3])

with col1:
    st.title("About Me")
    st.markdown(
  """Everyday engineer who possess strong interest in everything data :bar_chart:, cloud :cloud:, and emerging technologies :robot_face:.
  Someone who will enjoy being part of your Data/AI/ML team. """)

    st.markdown("""Currently invested in
    - Designing and integrating ETL/ELT pipelines
    - Collecting and cleaning data 
    - Finding insights and building dashboards
    - Developing and deploying ML models
     """)
    st.markdown("""\n""")
    st.markdown("""**Connect with me on** [**LinkedIn**](https://www.linkedin.com/in/mahipalzanakat) | [**GitHub**](https://github.com/mahipal-z) | [**Medium**](https://medium.com/@storiesbymahipal)
  """)
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

with col2:
    st.title("**Mahipal Zanakat**")
    st.image(image1)
######################
#sidebar layout
######################

st.sidebar.subheader("Portfolio")

            
