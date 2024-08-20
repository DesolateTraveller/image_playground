#---------------------------------------------------------------------------------------------------------------------------------
### Authenticator
#---------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
#---------------------------------------------------------------------------------------------------------------------------------
### Import Libraries
#---------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#----------------------------------------
import os
import sys
import io
import traceback
from PIL import Image
#----------------------------------------
from io import BytesIO
#----------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Title and description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title="Image Playground | v0.1",
                    layout="wide",
                    page_icon="🖼️",            
                    initial_sidebar_state="collapsed")
#----------------------------------------
st.title(f""":rainbow[Image Playground]""")
st.markdown(
    '''
    Created by | <a href="mailto:avijit.mba18@gmail.com">Avijit Chakraborty</a> ( :envelope: [Email](mailto:avijit.mba18@gmail.com) | :bust_in_silhouette: [LinkedIn](https://www.linkedin.com/in/avijit2403/) | :computer: [GitHub](https://github.com/DesolateTraveller) ) |
    for best view of the app, please **zoom-out** the browser to **75%**.
    ''',
    unsafe_allow_html=True)
st.info('**A lightweight image-processing streamlit app that supports the following operations: upload image, crop, remove background, mirror, convert, rotate, change brightness**', icon="ℹ️")

#----------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Functions & Definitions
#---------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Main app
#---------------------------------------------------------------------------------------------------------------------------------

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10  = st.tabs(["**Content**","**View**","**Crop**","**Remove**","**Mirror**","**Convert**","**Rotate**","**Change**","**Generate**","**Compare**"])

#---------------------------------------------------------------------------------------------------------------------------------
### Content
#---------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### View
#---------------------------------------------------------------------------------------------------------------------------------

with tab2:

    option = st.radio(
    label="Upload an image, take one with your camera, or load image from a URL",
    options=(
        "⬆️ Upload an image",
        "📷 Take a photo with my camera",
        "🌐 Load image from a URL",
    ),
    horizontal=True, label_visibility='collapsed',
    help="Uploaded images are deleted from the server when you\n* upload another image, or\n* clear the file uploader, or\n* close the browser tab",)

    if option == "⬆️ Upload an image":
        upload_img = st.file_uploader(label="Upload an image",type=["bmp", "jpg", "jpeg", "png", "svg"],)
        mode = "upload"

    elif option == "📷 Take a photo with my camera":
        upload_img = st.camera_input(label="Take a picture",)
        mode = "camera"

    elif option == "Load image from a URL 🌐":
        url = st.text_input("Image URL",key="url",)
        mode = "url"

        if url != "":
            try:
                response = requests.get(url)
                upload_img = Image.open(BytesIO(response.content))
            except:
                st.error("The URL does not seem to be valid.")
