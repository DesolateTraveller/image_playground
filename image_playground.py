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
import requests
import traceback
import contextlib
from PIL import Image, ImageEnhance, ImageOps
#----------------------------------------
from io import BytesIO
#----------------------------------------
#from rembg import remove
from st_social_media_links import SocialMediaIcons
from streamlit_cropper import st_cropper
from streamlit_image_comparison import image_comparison
#---------------------------------------------------------------------------------------------------------------------------------
### Title and description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title="Image Playground | v0.2",
                    layout="wide",
                    page_icon="🖼️",            
                    initial_sidebar_state="collapsed")
#----------------------------------------
#st.title(f""":rainbow[Image Playground]""")
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        background: linear-gradient(to left, red, orange, blue, indigo, violet);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    </style>
    <div class="title">Image Playground</div>
    """,
    unsafe_allow_html=True
)
#----------------------------------------

st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #F9F9FB;
        text-align: center;
        padding: 5px;
        font-size: 15px;
        color: #333;
        z-index: 100;
    }
    .footer p {
        margin: 0;
    }
    .footer .highlight {
        font-weight: bold;
        color: blue;
    }
    </style>

    <div class="footer">
        <p>© 2025 | Developed by: <span class="highlight">E&PT - Digital Solutions</span> | Prepared by: <a href="mailto:avijit.chakraborty@clariant.com">Avijit Chakraborty</a> & <a href="mailto:rakesh.lipare@clariant.com">Rakesh Lipare</a></p> 
        <span class="highlight">Thank you for visiting the app | This app is created for internal use, unauthorized uses or copying is strictly prohibited | For best view of the app, please zoom out the browser to 75%.</span>
    </div>
    
""", unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------------------------------------------
### Functions & Definitions
#---------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Main app
#---------------------------------------------------------------------------------------------------------------------------------
stats_expander = st.expander("**:blue[App Capabilities]**", expanded=False)
with stats_expander:

        st.markdown("""
            <style>
            .info-container {
            padding: 20px;
            background-color: #f9f9f9;
            border-left: 6px solid #3498db;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            }
            .info-container h3 {
            color: #3498db;
            font-weight: bold;
            margin-bottom: 10px;
            }
            .info-container p {
            color: #333;
            margin: 5px 0;
            }
            .info-container ul {
            list-style-type: none;
            padding: 0;
            }
            .info-container li {
            margin: 10px 0;
            display: flex;
            align-items: center;
            }
            .info-container li:before {
            content: "⭐";
            margin-right: 10px;
            color: #3498db;
            font-size: 1.2em;
            }
            </style>

            <div class="info-container">
            <h3>🛠️ App Capabilities</h3>
            <p>This app is designed to perform a variety of tasks including:</p>
            <ul>
            <li><strong>View</strong> -         It allows you to preview the uploaded image file directly within the application.</li>
            <li><strong>Crop</strong> -         It is designed to crop the uploaded image file.</li>
            <li><strong>Remove</strong> -       It helps to remove the background of the uploadedimage file.</li>
            <li><strong>Mirror</strong> -       It helps create mirror of the uploaded image file.</li>
            <li><strong>Convert</strong> -      It helps to convert in greyscale or black-white of the uploaded image file.</li>
            <li><strong>Rotate</strong> -       It helps to rotate of the uploaded image file.</li>
            <li><strong>Change</strong> -       It helps to change the brightness, saturation, contrast & sharpness of the uploaded image file.</li>
            <li><strong>Generate</strong> -     It tab allows to generate a random image from the uploaded image file. </li>                       
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
#---------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------

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
        upload_img = st.file_uploader(label="**Upload an image**",type=["bmp", "jpg", "jpeg", "png", "svg"],)
        mode = "upload"

elif option == "📷 Take a photo with my camera":
        upload_img = st.camera_input(label="**Take a picture**",)
        mode = "camera"

elif option == "🌐 Load image from a URL":
        url = st.text_input("**Image URL**",key="url",)
        mode = "url"

        if url != "":
            try:
                response = requests.get(url)
                upload_img = Image.open(BytesIO(response.content))
            except:
                st.error("The URL does not seem to be valid.")
                
with contextlib.suppress(NameError):
    if upload_img is not None:
        pil_img = (upload_img.convert("RGB") if mode == "url" else Image.open(upload_img).convert("RGB"))
        img_arr = np.asarray(pil_img)

        if mode == "upload":
            file_details = {
                "File Name": upload_img.name,
                "File Size (KB)": round(upload_img.size / 1024, 2),
                "Format": pil_img.format,
                "Mode": pil_img.mode,
                "Width (px)": pil_img.size[0],
                "Height (px)": pil_img.size[1],}
        else:
            file_details = {
                "File Name": "Captured Image" if mode == "camera" else os.path.basename(url),
                "File Size (KB)": "N/A",
                "Format": pil_img.format,
                "Mode": pil_img.mode,
                "Width (px)": pil_img.size[0],
                "Height (px)": pil_img.size[1],
                }

#---------------------------------------------------------------------------------------------------------------------------------
### Content
#---------------------------------------------------------------------------------------------------------------------------------

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["**View**","**Crop**","**Remove**","**Mirror**","**Convert**","**Rotate**","**Change**","**Generate**",])

#---------------------------------------------------------------------------------------------------------------------------------
### View
#---------------------------------------------------------------------------------------------------------------------------------

        with tab1:

            st.write("""
            The **View** tab allows you to preview image files directly within the application. 
            You can upload or take photo using camera of load from a URL of an image and view its content without any external software.
            """)
            col1, col2 = st.columns((0.8,0.2))
            with col1:
                
                st.subheader("Image", divider='blue')
                st.image(img_arr, use_column_width="auto", caption="Uploaded Image")

                with col2:
                     
                    st.subheader("Information", divider='blue')
                    for key, value in file_details.items():
                        st.write(f"**{key}:** {value}")
                    #st.write(f"Original width = {pil_img.size[0]}px and height = {pil_img.size[1]}px")

#---------------------------------------------------------------------------------------------------------------------------------
### Crop
#---------------------------------------------------------------------------------------------------------------------------------

        with tab2:

            st.write("""
            The **Crop** tab is designed to crop the uploaded image files. 
            You can upload or take photo using camera of load from a URL of an image and the tool will help to crop the image file.
            """) 
            col1, col2, col3 = st.columns((0.1,0.6,0.3))
            with col1:

                st.subheader("Parameters", divider='blue')                 
                realtime_update = st.checkbox(label="**update in Real Time**", value=True)
                box_color = st.color_picker(label="**Box Color**", value='#0000FF')
                aspect_choice = st.radio(label="**Aspect Ratio**", options=["1:1", "16:9", "4:3", "2:3", "Free"])
                aspect_dict = {"1:1": (1, 1),"16:9": (16, 9),"4:3": (4, 3),"2:3": (2, 3),"Free": None}
                aspect_ratio = aspect_dict[aspect_choice]

            with col2:

                st.subheader("Image", divider='blue')
                img = Image.fromarray(img_arr)
                if not realtime_update:
                    st.write("**Double click to save crop**")
                cropped_img = st_cropper(img, realtime_update=realtime_update, box_color=box_color,aspect_ratio=aspect_ratio)
                #st.image(img_arr, use_column_width="auto", caption="Original Image")
                #cropped_img = st_cropper(Image.fromarray(img_arr), should_resize_image=True)

                with col3:

                    #if st.button("**Crop Image**"):
                        st.subheader("Output", divider='blue')                      
                        st.image(cropped_img, use_column_width="auto", caption="Cropped Image")
                        st.write(f"Cropped width = {cropped_img.size[0]}px and height = {cropped_img.size[1]}px")

                        buffered = BytesIO()
                        cropped_img.save(buffered, format="PNG")
                        st.download_button(label="**Download Cropped Image**",data=buffered,file_name="cropped_image.png",mime="image/png",)

                        if "cropped_img" not in locals():
                            st.write(f"Original width = {pil_img.size[0]}px and height = {pil_img.size[1]}px")

#---------------------------------------------------------------------------------------------------------------------------------
### Remove
#---------------------------------------------------------------------------------------------------------------------------------

        with tab3:

            st.write("""
            The **Remove** tab is designed to remove the background of the uploaded image files. 
            You can upload or take photo using camera of load from a URL of an image and the tool will help to remove the background of the image file.
            """) 
            col1, col2 = st.columns((0.6, 0.4))
            with col1:

                st.subheader("Image", divider='blue')             
                st.image(img_arr, use_column_width="auto", caption="Original Image")

                with col2:
                        
                    st.subheader("Output", divider='blue')  
                    if st.button("**Remove Background**"):
                        bg_removed_img = remove(pil_img)
                        st.image(bg_removed_img, use_column_width="auto", caption="Background Removed")

                        buffered = BytesIO()
                        bg_removed_img.save(buffered, format="PNG")
                        st.download_button(label="**Download Image with Background Removed**",data=buffered,file_name="bg_removed_image.png",mime="image/png",)

#---------------------------------------------------------------------------------------------------------------------------------
### Mirror
#---------------------------------------------------------------------------------------------------------------------------------

        with tab4:

            st.write("""
            The **Mirror** tab is designed to mirror the uploaded image files. 
            You can upload or take photo using camera of load from a URL of an image and the tool will help to mirror of the image file.
            """)                          
            col1, col2 = st.columns((0.6, 0.4))
            with col1:

                st.subheader("Image", divider='blue')             
                st.image(img_arr, use_column_width="auto", caption="Original Image")

                with col2:

                    st.subheader("Output", divider='blue')                       
                    if st.button("**Mirror Image**"):
                        mirrored_img = ImageOps.mirror(pil_img)
                        st.image(mirrored_img, use_column_width="auto", caption="Mirrored Image")

                        buffered = BytesIO()
                        mirrored_img.save(buffered, format="PNG")
                        st.download_button(label="**Download Mirrored Image**",data=buffered,file_name="mirrored_image.png",mime="image/png",)

#---------------------------------------------------------------------------------------------------------------------------------
### Convert
#---------------------------------------------------------------------------------------------------------------------------------

        with tab5:

            st.write("""
            The **Convert** tab is designed to convert of the uploaded image files. 
            You can upload or take photo using camera of load from a URL of an image and the tool will help to convert of the image file to either black-&-white or greyscale.
            """)                                   
            col1, col2 = st.columns((0.6, 0.4))
            with col1:            

                st.subheader("Image", divider='blue')             
                st.image(img_arr, use_column_width="auto", caption="Original Image")

                with col2:

                    st.subheader("Output", divider='blue')                       
                    conv_option = st.radio('Options', ['BW','Greyscale'], horizontal=True, label_visibility='collapsed', key='conv_option')

                    if conv_option == "BW":
                        bw_img = pil_img.convert("1")  
                        st.image(bw_img, use_column_width="auto", caption="Black & White Image")
                        buffered = BytesIO()
                        bw_img.save(buffered, format="PNG")
                        st.download_button(label="**Download Black & White Image**",data=buffered,file_name="black_white_image.png",mime="image/png",)

                    if conv_option == "Greyscale":
                        grey_img = pil_img.convert("L") 
                        st.image(grey_img, use_column_width="auto", caption="Greyscale Image")
                        buffered = BytesIO()
                        grey_img.save(buffered, format="PNG")
                        st.download_button(label="**Download Greyscale Image**",data=buffered,file_name="greyscale_image.png",mime="image/png",)

#---------------------------------------------------------------------------------------------------------------------------------
### Rotate
#---------------------------------------------------------------------------------------------------------------------------------

        with tab6:

            st.write("""
            The **Rotate** tab is designed to rotate of the uploaded image files. 
            You can upload or take photo using camera of load from a URL of an image and the tool will help to rotate of the image file.
            """)                     
            col1, col2 = st.columns((0.6, 0.4))
            with col1:            

                st.subheader("Image", divider='blue')             
                st.image(img_arr, use_column_width="auto", caption="Original Image")

                with col2:

                    st.subheader("Output", divider='blue')                       
                    angle = st.slider("Rotate Image", min_value=0, max_value=360, value=0)
                    if st.button("**Rotate Image**"):
                         
                        rotated_img = pil_img.rotate(angle)
                        st.image(rotated_img, use_column_width="auto", caption=f"Rotated Image by {angle} degrees")
        
                        buffered = BytesIO()
                        rotated_img.save(buffered, format="PNG")
                        st.download_button(label="**Download Rotated Image**",data=buffered,file_name="rotated_image.png",mime="image/png",)

#---------------------------------------------------------------------------------------------------------------------------------
### Change
#---------------------------------------------------------------------------------------------------------------------------------

        with tab7:

            st.write("""
            The **Change** tab is designed to change the properties of the uploaded image files. 
            You can upload or take photo using camera of load from a URL of an image and the tool will help to change the properties (e.g, brightness,saturation, sharpness, contrast) of the image file.
            """)                 
            col1, col2 = st.columns((0.6, 0.4))
            with col1:            

                st.subheader("Image", divider='blue')             
                st.image(img_arr, use_column_width="auto", caption="Original Image")

                with col2:

                    st.subheader("Output", divider='blue')  
                    stats_expander = st.expander("**:blue[Tuner]**", expanded=False)
                    with stats_expander:
                        brightness = st.slider("Brightness", 0.0, 2.0, 1.0)
                        saturation = st.slider("Saturation", 0.0, 2.0, 1.0)
                        sharpness = st.slider("Sharpness", 0.0, 2.0, 1.0)
                        contrast = st.slider("Contrast", 0.0, 2.0, 1.0)

                    enhanced_img = ImageEnhance.Brightness(pil_img).enhance(brightness)
                    enhanced_img = ImageEnhance.Color(enhanced_img).enhance(saturation)
                    enhanced_img = ImageEnhance.Sharpness(enhanced_img).enhance(sharpness)
                    enhanced_img = ImageEnhance.Contrast(enhanced_img).enhance(contrast)
                    st.image(enhanced_img, use_column_width="auto", caption="Contrast Adjusted")

                    buffered = BytesIO()
                    enhanced_img.save(buffered, format="PNG")
                    st.download_button(label="**Download Adjusted Image**",data=buffered,file_name="adjusted_image.png",mime="image/png",)

#---------------------------------------------------------------------------------------------------------------------------------
### Generate
#---------------------------------------------------------------------------------------------------------------------------------

        with tab8:

            st.write("""
            The **Generate** tab is designed to generate new images based on the uploaded image files. 
            You can upload or take photo using camera of load from a URL of an image and the tool will help to generate new images based on the the image file.
            """)   
            st.info('**Disclaimer : This portion is under Development**', icon="ℹ️") 
