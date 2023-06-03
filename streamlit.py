

import streamlit as st
from PIL import Image

image1 = Image.open('Photo Web.jpg')

st.set_page_config( 
    page_title="Mahipal Zanakat",
    page_icon=image1 
)


######################
#main page layout
######################

st.title("About Me")

st.markdown(
  """Everyday engineer fully invested in Data Analytics and Cloud Technology in the past few years.
     \nSomeone who will enjoy being part of your Data/AI/ML team. """)

st.markdown("""Experienced in:
- Collecting and Cleaning Data 
- Finding insights and building Dashboards
- Building and Deploying ML Models
     """
)

st.divider()
st.subheader("Connect with Me")

st.markdown(
  """LinkedIn
  \nGitHub
  \nMedium
  """
)
st.divider()

st.subheader("I could be a good company if")

st.markdown("""
- You challenge me for a game of Chess: @mahipalzankat chess.com
- Or Hiking nearby or trying a new restaurant
- Or Bowling, Lifting Weights, Card games, Board games or Cooking
- Or you are willing to teach me Swimming, Golfing, or Piano
"""
)            


######################
#sidebar layout
######################

st.sidebar.title("Mahipal Zanakat")
st.sidebar.image(image1, width=250)
            
st.sidebar.write("Portfolio")

            
