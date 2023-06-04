

import streamlit as st
from PIL import Image

image1 = Image.open('Photo Web.jpg')
image2 = Image.open('Photo May2020.jpg')

st.set_page_config( 
    page_title="Mahipal Zanakat",
    page_icon=image2 
)


######################
#main page layout
######################

st.title("About Me")

st.markdown(
  """Everyday engineer who possess strong interest in everything data :bar_chart:, cloud :cloud:, and emerging technologies :robot_face:.
  Someone who will enjoy being part of your Data/AI/ML team. """)

st.markdown("""Currently invested in
- Designing and integrating ETL/ELT pipelines
- Collecting and cleaning data 
- Finding insights and building dashboards
- Developing and deploying ML models
     """
)
st.markdown("""\n""")
st.markdown("""**Connect with me on** [**LinkedIn**](https://www.linkedin.com/in/mahipalzanakat) | [**GitHub**](https://github.com/mahipal-z) | [**Medium**](https://medium.com/@storiesbymahipal)
  """)
st.divider()

#col1, col2 = st.columns([1, 1])

#with col1:


#with col2:
st.subheader("I could be a good company if")
st.markdown("""
You challenge me to a game of Chess :chess_pawn: [@chess.com](https://friend.chess.com/W7Xra)
\nOr Hiking :runner: nearby or trying a new restaurant :shallow_pan_of_food:
\nOr Bowling :bowling:, Lifting Weights :weight_lifter:, Card games, Board games :game_die:, or for Cooking
\nOr you are willing to teach me Swimming :swimmer:, Golfing :golfer:, Pool :8ball:, or Piano :musical_keyboard:
"""
)

st.divider()

st.subheader("Certification")


st.divider()
st.subheader("Education")

st.markdown("""**Master of Engineering, Mechanical | University of Ottawa**
         \n**Data Scientist in Python | DataCamp**
         \n**Data Analst in SQL | DataCamp**
         \n**Machine Learning by Andrew Ng. | Stanford University**""")


######################
#sidebar layout
######################

st.sidebar.title("**Mahipal Zanakat**")
st.sidebar.image(image1)
            
st.sidebar.subheader("Portfolio")

            
