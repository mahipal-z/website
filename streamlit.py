

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
  """Everyday engineer who possess strong interest in everything data, cloud :cloud: and emerging technologies.
  Someone who will enjoy being part of your Data/AI/ML team. """)

st.markdown("""Currently invested in
- Designing and integrating ETL/ELT pipelines
- Collecting and cleaning data 
- Finding insights and building dashboards
- Developing and deploying ML models
     """
)

st.divider()
st.subheader("Connect with Me")

st.write(
  """[:blue[LinkedIn]](https://www.linkedin.com/in/mahipalzanakat) | [**GitHub**](https://github.com/mahipal-z) | [:violet[Medium]](https://medium.com/@storiesbymahipal)
  """
)
st.divider()

st.subheader("I could be a good company if")

st.markdown("""
- You challenge me to a game of Chess :chess_pawn: [@mahipalzankat on chess.come](https://friend.chess.com/W7Xra)
- Or Hiking :runner: nearby or trying a new restaurant :shallow_pan_of_food:
- Or Bowling, :bowling: Lifting Weights, :weight_lifter: Card games, Board games, :game_die: or Cooking
- Or you are willing to teach me Swimming, :swimmer: Golfing, :golfer: Pool, :8ball: or Piano :musical_keyboard:
"""
)            


######################
#sidebar layout
######################

st.sidebar.title("**Mahipal Zanakat**")
st.sidebar.image(image1, width=250)
            
st.sidebar.write("**Portfolio**")

            
