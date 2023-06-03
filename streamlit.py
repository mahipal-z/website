

import streamlit as st
from PIL import Image

image1 = Image.open('Photo May2020.jpg')

st.set_page_config( 
    page_title="Mahipal Zanakat",
    page_icon=image1 
)


######################
#main page layout
######################

st.title("About Me")

st.markdown(
  """Everyday engineer fully invested in the Data Analytics and Cloud Technology since past few years.
     \nSomeone who will enjoy to be part of the Data Team in your organization. 
     \nExperienced in:
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

st.subheader("I could be a good company:")

st.markdown("""
- if you challenge me for a game of Chess: @mahipalzankat chess.com
- Outdoors: Hiking nearby, Trying new food
- Indoors: Bowling, Lifting Weights, Card games, Board games and Cooking
- Looking forward to learn some day: Swimming, Golfing, Piano
"""
)            


######################
#sidebar layout
######################

st.sidebar.title("Mahipal Zanakat")
st.sidebar.image(image1, width=250)
            
st.sidebar.write("Portfolio")

            
