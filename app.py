import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports 
from multipage import MultiPage
from pages import about, howtouse, main, portfolio # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
display = Image.open('Logo.png')
display = np.array(display)
# st.image(display, width = 400)
# st.title("Data Storyteller Application")
col1, col2 = st.beta_columns(2)
col1.image(display, width = 400)
col2.title("Data Storyteller Application")

# Add all your application here
app.add_page("Upload Data", howtouse.app)
app.add_page("Change Metadata", about.app)
app.add_page("Machine Learning", main.app)
app.add_page("Data Analysis",portfolio.app)


# The main app
app.run()