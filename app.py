import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports 
from multipage import MultiPage
from pages import about, howtouse, analysis, socialAnalysis, main, portfolio # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
# display = Image.open('Logo.png')
# display = np.array(display)
# st.image(display, width = 400)
# st.title("Data Storyteller Application")
# col1.image(display, width = 400)
st.set_page_config(layout="wide")
st.title("Cryptocurrency Analysis And Management")

# Add all your application here
app.add_page("Home", main.app)
app.add_page("Analysis",analysis.app)
app.add_page("Social Analysis", socialAnalysis.app)
app.add_page("Portfolio",portfolio.app)
app.add_page("How To Use", howtouse.app)
app.add_page("About Us", about.app)
# The main app
app.run()