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
from rembg import remove
#from st_social_media_links import SocialMediaIcons
from streamlit_cropper import st_cropper
#from streamlit_image_comparison import image_comparison
#---------------------------------------------------------------------------------------------------------------------------------
### Title and description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title="Image Playground | v0.2",
                    layout="wide",
                    page_icon="🖼️",            
                    initial_sidebar_state="collapsed")
#---------------------------------------------------------------------------------------------------------------------------------
### Login Page | Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------

             
#---------------------------------------------------------------------------------------------------------------------------------
### CSS
#---------------------------------------------------------------------------------------------------------------------------------

             
#---------------------------------------------------------------------------------------------------------------------------------
### Description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .title-large {
        text-align: center;
        font-size: 35px;
        font-weight: bold;
        background: linear-gradient(to left, red, orange, blue, indigo, violet);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .title-small {
        text-align: center;
        font-size: 20px;
        background: linear-gradient(to left, red, orange, blue, indigo, violet);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .version-badge {
        text-align: center;
        display: inline-block;
        background: linear-gradient(120deg, #0056b3, #0d4a96);
        color: white;
        padding: 2px 12px;
        border-radius: 20px;
        font-size: 1.15rem;
        margin-top: 8px;
        font-weight: 600;
        letter-spacing: 0.5px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    }
    </style>
    <div style="text-align: center;">
        <div class="title-large">Image Playground</div>
        <div class="version-badge"> Play with Image | v0.2 </div>
    </div>
    """,
    unsafe_allow_html=True
)
#----------------------------------------
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #F0F2F6;
        text-align: center;
        padding: 10px;
        font-size: 14px;
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
        <p>© 2026 | Created by : <span class="highlight">Avijit Chakraborty</span> <a href="mailto:avijit.mba18@gmail.com"> 📩 </a> | <span class="highlight">Thank you for visiting the app | Unauthorized uses or copying is strictly prohibited | For best view of the app, please zoom out the browser to 75%.</span> </p>
    </div>
    """,
    unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------
### Functions & Definitions
#---------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------
### Main app
#---------------------------------------------------------------------------------------------------------------------------------

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_home():
    st.session_state.page = 'home'

#---------------------------------------------------------------------------------------------------------------------------------
if st.session_state.page == 'home':

    st.markdown("""
    <style>
    .banner {
        background: linear-gradient(135deg, #f0f7ff 0%, #e6f2ff 100%);
        border-radius: 32px;
        padding: 15px;
        margin: 25px 0;
        border: 1px solid rgba(0, 86, 179, 0.15);
        text-align: center;
        font-size: 1.15rem;
        color: #0056b3;
        font-weight: 600;
    }
    </style>

    <div class="banner">
        Click the cards below to access different sections and explore the following features
    </div>
    """, unsafe_allow_html=True)
    
    def render_tool_card(col, title, icon, description, page_key, button_key):
        with col:
            st.markdown(f"""
            <div class="card" style="
                border: 1px solid #e0e0e0; 
                border-radius: 12px; 
                padding: 20px; 
                height: 100%; 
                background-color: #ffffff;
                box-shadow: 0 2px 5px rgba(0,0,0,0.05);
                transition: transform 0.2s, box-shadow 0.2s;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            ">
                <div>
                    <div class="card-title" style="
                        font-size: 1.2em; 
                        font-weight: 700; 
                        margin-bottom: 12px; 
                        color: #2c3e50;
                        display: flex;
                        align-items: center;
                        gap: 8px;
                    ">
                        <span style="font-size: 1.4em;">{icon}</span> {title}
                    </div>
                    <ul class="card-list" style="list-style: none; padding: 0; margin: 0; font-size: 0.9em; color: #555;">
                        <li>{description}</li>
                    </ul>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("**🚀 Click to Enter**", key=button_key, use_container_width=True, type="primary"):
                st.session_state.page = page_key
                st.rerun()

    cols_row1 = st.columns(4)

    render_tool_card(cols_row1[0], "View", "👁️", "Preview uploaded images directly within the application.", 'img_view', 'btn_img_view')
    render_tool_card(cols_row1[1], "Crop", "✂️", "Crop images to specific dimensions easily.", 'img_crop', 'btn_img_crop')
    render_tool_card(cols_row1[2], "Remove BG", "🧹", "Remove backgrounds from images automatically.", 'img_remove', 'btn_img_remove')
    render_tool_card(cols_row1[3], "Mirror", "🪞", "Create mirror reflections of your images.", 'img_mirror', 'btn_img_mirror')

    st.write("") # Spacer between rows

    cols_row2 = st.columns(4)

    render_tool_card(cols_row2[0], "Convert", "🎨", "Convert images to grayscale or black & white.", 'img_convert', 'btn_img_convert')
    render_tool_card(cols_row2[1], "Rotate", "🔄", "Rotate images to any angle effortlessly.", 'img_rotate', 'btn_img_rotate')
    render_tool_card(cols_row2[2], "Adjust", "🔆", "Adjust brightness, saturation, contrast & sharpness.", 'img_adjust', 'btn_img_adjust')
    render_tool_card(cols_row2[3], "Generate", "✨", "Generate random variations from uploaded images.", 'img_generate', 'btn_img_generate')

#---------------------------------------------------------------------------------------------------------------------------------
### View
#---------------------------------------------------------------------------------------------------------------------------------

#with tab1:
#if page == "view": 
elif st.session_state.page == 'img_view':

    st.markdown("---")      
    col_home, title= st.columns([2,15,])
            
    with col_home:
        if st.button("Home", icon="🏠", key="home_fd", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    with title:
        st.info("""The **View** tab allows you to preview image files directly within the application. You can upload an image, take a photo using your camera, or load an image from a URL and view its content without any external software.""")

    col1, col2, col3 = st.columns((0.15,0.45,0.4))
    with col1:
        with st.container(border=True):
            
            option = st.radio(
                label="Upload an image, take one with your camera, or load an image from a URL",
                options=(
                    "⬆️ **:blue[Upload an image]**",
                    "📷 **:blue[Take a photo]**",
                    "🌐 **:blue[Load image from a URL]**",),
                label_visibility="collapsed", help="Uploaded images are deleted from the server when you\n""* upload another image, or\n""* clear the file uploader, or\n""* close the browser tab",)

            st.divider()
            upload_img = None  
            pil_img = None
            mode = None

            if option == "⬆️ **:blue[Upload an image]**":
                upload_img = st.file_uploader(label="**:blue[Upload an image]**",type=["bmp", "jpg", "jpeg", "png", "svg"],)
                mode = "upload"

            elif option == "📷 **:blue[Take a photo]**":
                enable = st.checkbox("Enable camera")
                upload_img = st.camera_input(label="**:blue[Take a picture]**", disabled=not enable)
                mode = "camera"

            elif option == "🌐 **:blue[Load image from a URL]**":
                url = st.text_input("**:blue[Image URL]**", key="url")
                mode = "url"
                if url:
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            upload_img = Image.open(BytesIO(response.content))  
                        else:
                            st.error("Failed to load image from URL.")
                    except Exception as e:
                        st.error(f"Error loading image: {e}")

            if upload_img is not None:

                if mode == "upload" or mode == "camera":
                    pil_img = Image.open(upload_img).convert("RGB")
                elif mode == "url":
                    pil_img = upload_img.convert("RGB")  # Since upload_img is already an Image object
                img_arr = np.asarray(pil_img)  # Convert PIL Image to NumPy array for display

                if mode == "upload":
                    file_details = {"File Name": upload_img.name,"File Size (KB)": round(upload_img.size / 1024, 2),
                    "Format": pil_img.format,"Mode": pil_img.mode,"Width (px)": pil_img.size[0],"Height (px)": pil_img.size[1],}
                else:
                    file_details = {"File Name": "Captured Image" if mode == "camera" else os.path.basename(url),
                    "File Size (KB)": "N/A","Format": pil_img.format,"Mode": pil_img.mode,"Width (px)": pil_img.size[0],"Height (px)": pil_img.size[1],}

                st.success("Image loaded successfully!")
                
                with col2:
                    with st.container(border=True):
                
                        st.image(img_arr, use_container_width="auto", caption="Uploaded Image")
        
                with col3:
                    with st.container(border=True):
                
                        for key, value in file_details.items():
                            st.write(f"**{key}:** {value}")
                    
            else:
                st.warning("Please upload/click/fetch a image file to view.")

#---------------------------------------------------------------------------------------------------------------------------------
### Crop
#---------------------------------------------------------------------------------------------------------------------------------

#with tab2:
#if page == "crop":
elif st.session_state.page == 'img_crop':

    st.markdown("---")      
    col_home, title= st.columns([2,15,])
            
    with col_home:
        if st.button("Home", icon="🏠", key="home_fd", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    with title:    
        st.info("""The **Crop** tab is designed to crop the uploaded image files. You can upload or take photo using camera of load from a URL of an image and the tool will help to crop the image file.""") 
        
    col1, col2, col3 = st.columns((0.15,0.45,0.4))
    with col1:
        with st.container(border=True):
            
            option = st.radio(
                label="Upload an image, take one with your camera, or load an image from a URL",
                options=(
                    "⬆️ **:blue[Upload an image]**",
                    "📷 **:blue[Take a photo]**",
                    "🌐 **:blue[Load image from a URL]**",),
                label_visibility="collapsed", help="Uploaded images are deleted from the server when you\n""* upload another image, or\n""* clear the file uploader, or\n""* close the browser tab",)

            st.divider()
            upload_img = None  # Ensure upload_img is always defined
            pil_img = None
            mode = None

            if option == "⬆️ **:blue[Upload an image]**":
                upload_img = st.file_uploader(label="**:blue[Upload an image]**",type=["bmp", "jpg", "jpeg", "png", "svg"],)
                mode = "upload"

            elif option == "📷 **:blue[Take a photo]**":
                enable = st.checkbox("Enable camera")
                upload_img = st.camera_input(label="**:blue[Take a picture]**", disabled=not enable)
                mode = "camera"

            elif option == "🌐 **:blue[Load image from a URL]**":
                url = st.text_input("**:blue[Image URL]**", key="url")
                mode = "url"
                if url:
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            upload_img = Image.open(BytesIO(response.content))  # Directly set upload_img
                        else:
                            st.error("Failed to load image from URL.")
                    except Exception as e:
                        st.error(f"Error loading image: {e}")

            if upload_img is not None:

                if mode == "upload" or mode == "camera":
                    pil_img = Image.open(upload_img).convert("RGB")
                elif mode == "url":
                    pil_img = upload_img.convert("RGB")  # Since upload_img is already an Image object
                img_arr = np.asarray(pil_img)  # Convert PIL Image to NumPy array for display

                if mode == "upload":
                    file_details = {"File Name": upload_img.name,"File Size (KB)": round(upload_img.size / 1024, 2),
                    "Format": pil_img.format,"Mode": pil_img.mode,"Width (px)": pil_img.size[0],"Height (px)": pil_img.size[1],}
                else:
                    file_details = {"File Name": "Captured Image" if mode == "camera" else os.path.basename(url),
                    "File Size (KB)": "N/A","Format": pil_img.format,"Mode": pil_img.mode,"Width (px)": pil_img.size[0],"Height (px)": pil_img.size[1],}
                    
                st.success("Image loaded successfully!")
                
                #st.subheader("Parameters", divider='blue')   
                st.divider()             
                realtime_update = st.checkbox(label="**update in Real Time**", value=True)
                box_color = st.color_picker(label="**Box Color**", value='#0000FF')
                aspect_choice = st.radio(label="**Aspect Ratio**", options=["1:1", "16:9", "4:3", "2:3", "Free"],horizontal=True)
                aspect_dict = {"1:1": (1, 1),"16:9": (16, 9),"4:3": (4, 3),"2:3": (2, 3),"Free": None}
                aspect_ratio = aspect_dict[aspect_choice]
                    
                with col2:
                    with st.container(border=True):

                        #st.subheader("Image", divider='blue')
                        img = Image.fromarray(img_arr)
                        if not realtime_update:
                            st.write("**Double click to save crop**")
                        cropped_img = st_cropper(img,realtime_update=realtime_update,box_color=box_color,aspect_ratio=aspect_ratio)
                        #st.image(img_arr, use_container_width="auto", caption="Original Image")
                        #cropped_img = st_cropper(Image.fromarray(img_arr), should_resize_image=True)

                with col3:
                    with st.container(border=True):
                        
                        #if st.button("**Crop Image**"):
                        #st.subheader("Output", divider='blue')                      
                        st.image(cropped_img, use_container_width="auto", caption="Cropped Image")
                        st.write(f"Cropped width = {cropped_img.size[0]}px and height = {cropped_img.size[1]}px")

                        buffered = BytesIO()
                        cropped_img.save(buffered, format="PNG")
                    st.download_button(label="**📥 Download Cropped Image**",data=buffered,file_name="cropped_image.png",mime="image/png",)

                    if "cropped_img" not in locals():
                        st.write(f"Original width = {pil_img.size[0]}px and height = {pil_img.size[1]}px")
                        
            else:
                st.warning("Please upload/click/fetch a image file to crop.")

#---------------------------------------------------------------------------------------------------------------------------------
### Remove
#---------------------------------------------------------------------------------------------------------------------------------

#with tab3:
#if page == "remove":
elif st.session_state.page == 'img_remove':

    st.markdown("---")      
    col_home, title= st.columns([2,15,])
            
    with col_home:
        if st.button("Home", icon="🏠", key="home_fd", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    with title:       
        st.info("""The **Remove** tab is designed to remove the background of the uploaded image files. You can upload or take photo using camera of load from a URL of an image and the tool will help to remove the background of the image file.""") 
    
    col1, col2, col3 = st.columns((0.15,0.45,0.4))
    with col1:
        with st.container(border=True):
            
            option = st.radio(
                label="Upload an image, take one with your camera, or load an image from a URL",
                options=(
                    "⬆️ **:blue[Upload an image]**",
                    "📷 **:blue[Take a photo]**",
                    "🌐 **:blue[Load image from a URL]**",),
                label_visibility="collapsed", help="Uploaded images are deleted from the server when you\n""* upload another image, or\n""* clear the file uploader, or\n""* close the browser tab",)

            st.divider()
            upload_img = None  # Ensure upload_img is always defined
            pil_img = None
            mode = None

            if option == "⬆️ **:blue[Upload an image]**":
                upload_img = st.file_uploader(label="**:blue[Upload an image]**",type=["bmp", "jpg", "jpeg", "png", "svg"],)
                mode = "upload"

            elif option == "📷 **:blue[Take a photo]**":
                enable = st.checkbox("Enable camera")
                upload_img = st.camera_input(label="**:blue[Take a picture]**", disabled=not enable)
                mode = "camera"

            elif option == "🌐 **:blue[Load image from a URL]**":
                url = st.text_input("**:blue[Image URL]**", key="url")
                mode = "url"
                if url:
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            upload_img = Image.open(BytesIO(response.content))  # Directly set upload_img
                        else:
                            st.error("Failed to load image from URL.")
                    except Exception as e:
                        st.error(f"Error loading image: {e}")

            if upload_img is not None:

                if mode == "upload" or mode == "camera":
                    pil_img = Image.open(upload_img).convert("RGB")
                elif mode == "url":
                    pil_img = upload_img.convert("RGB")  # Since upload_img is already an Image object
                img_arr = np.asarray(pil_img)  # Convert PIL Image to NumPy array for display

                if mode == "upload":
                    file_details = {"File Name": upload_img.name,"File Size (KB)": round(upload_img.size / 1024, 2),
                    "Format": pil_img.format,"Mode": pil_img.mode,"Width (px)": pil_img.size[0],"Height (px)": pil_img.size[1],}
                else:
                    file_details = {"File Name": "Captured Image" if mode == "camera" else os.path.basename(url),
                    "File Size (KB)": "N/A","Format": pil_img.format,"Mode": pil_img.mode,"Width (px)": pil_img.size[0],"Height (px)": pil_img.size[1],}

                st.success("Image loaded successfully!")
                if st.button("**Remove Background**"):
                    with col2:
                        with st.container(border=True):
            
                            st.image(img_arr, use_container_width="auto", caption="Original Image")

                    with col3:
                        with st.container(border=True):                        

                            bg_removed_img = remove(pil_img)
                            st.image(bg_removed_img, use_container_width="auto", caption="Background Removed")

                            buffered = BytesIO()
                            bg_removed_img.save(buffered, format="PNG")
                        st.download_button(label="**📥 Download Image with Background Removed**",data=buffered,file_name="bg_removed_image.png",mime="image/png",)
                        
            else:
                st.warning("Please upload/click/fetch a image file to remove.")

#---------------------------------------------------------------------------------------------------------------------------------
### Mirror
#---------------------------------------------------------------------------------------------------------------------------------

#with tab4:
#if page == "mirror":
elif st.session_state.page == 'img_mirror':

    st.markdown("---")      
    col_home, title= st.columns([2,15,])
            
    with col_home:
        if st.button("Home", icon="🏠", key="home_fd", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    with title:       
        st.info("""The **Mirror** tab is designed to mirror the uploaded image files. You can upload or take photo using camera of load from a URL of an image and the tool will help to mirror of the image file.""")                          
    
    col1, col2, col3 = st.columns((0.15,0.45,0.4))
    with col1:
        with st.container(border=True):
            
            option = st.radio(
                label="Upload an image, take one with your camera, or load an image from a URL",
                options=(
                    "⬆️ **:blue[Upload an image]**",
                    "📷 **:blue[Take a photo]**",
                    "🌐 **:blue[Load image from a URL]**",),
                label_visibility="collapsed", help="Uploaded images are deleted from the server when you\n""* upload another image, or\n""* clear the file uploader, or\n""* close the browser tab",)

            st.divider()
            upload_img = None  # Ensure upload_img is always defined
            pil_img = None
            mode = None

            if option == "⬆️ **:blue[Upload an image]**":
                upload_img = st.file_uploader(label="**:blue[Upload an image]**",type=["bmp", "jpg", "jpeg", "png", "svg"],)
                mode = "upload"

            elif option == "📷 **:blue[Take a photo]**":
                enable = st.checkbox("Enable camera")
                upload_img = st.camera_input(label="**:blue[Take a picture]**", disabled=not enable)
                mode = "camera"

            elif option == "🌐 **:blue[Load image from a URL]**":
                url = st.text_input("**:blue[Image URL]**", key="url")
                mode = "url"
                if url:
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            upload_img = Image.open(BytesIO(response.content))  # Directly set upload_img
                        else:
                            st.error("Failed to load image from URL.")
                    except Exception as e:
                        st.error(f"Error loading image: {e}")

            if upload_img is not None:

                if mode == "upload" or mode == "camera":
                    pil_img = Image.open(upload_img).convert("RGB")
                elif mode == "url":
                    pil_img = upload_img.convert("RGB")  # Since upload_img is already an Image object
                img_arr = np.asarray(pil_img)  # Convert PIL Image to NumPy array for display

                if mode == "upload":
                    file_details = {"File Name": upload_img.name,"File Size (KB)": round(upload_img.size / 1024, 2),
                    "Format": pil_img.format,"Mode": pil_img.mode,"Width (px)": pil_img.size[0],"Height (px)": pil_img.size[1],}
                else:
                    file_details = {"File Name": "Captured Image" if mode == "camera" else os.path.basename(url),
                    "File Size (KB)": "N/A","Format": pil_img.format,"Mode": pil_img.mode,"Width (px)": pil_img.size[0],"Height (px)": pil_img.size[1],}

                st.success("Image loaded successfully!")
                if st.button("**Mirror Image**"):
                    with col2:
                        with st.container(border=True):
            
                            st.image(img_arr, use_container_width="auto", caption="Original Image")

                    with col3:
                        with st.container(border=True):
                 
                            mirrored_img = ImageOps.mirror(pil_img)
                            st.image(mirrored_img, use_container_width="auto", caption="Mirrored Image")
                            buffered = BytesIO()
                            mirrored_img.save(buffered, format="PNG")
                            
                        st.download_button(label="**📥 Download Mirrored Image**",data=buffered,file_name="mirrored_image.png",mime="image/png",)

            else:
                st.warning("Please upload/click/fetch a image file to mirror.")
                
#---------------------------------------------------------------------------------------------------------------------------------
### Convert
#---------------------------------------------------------------------------------------------------------------------------------

#with tab5:
#if page == "convert":
elif st.session_state.page == 'img_convert':

    st.markdown("---")      
    col_home, title= st.columns([2,15,])
            
    with col_home:
        if st.button("Home", icon="🏠", key="home_fd", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    with title:       
        st.info("""The **Convert** tab is designed to convert of the uploaded image files. You can upload or take photo using camera of load from a URL of an image and the tool will help to convert of the image file to either black-&-white or greyscale.""")                                   
    
    col1, col2, col3 = st.columns((0.15,0.45,0.4))
    with col1:
        with st.container(border=True):
            
            option = st.radio(
                label="Upload an image, take one with your camera, or load an image from a URL",
                options=(
                    "⬆️ **:blue[Upload an image]**",
                    "📷 **:blue[Take a photo]**",
                    "🌐 **:blue[Load image from a URL]**",),
                label_visibility="collapsed", help="Uploaded images are deleted from the server when you\n""* upload another image, or\n""* clear the file uploader, or\n""* close the browser tab",)

            st.divider()
            upload_img = None  # Ensure upload_img is always defined
            pil_img = None
            mode = None

            if option == "⬆️ **:blue[Upload an image]**":
                upload_img = st.file_uploader(label="**:blue[Upload an image]**",type=["bmp", "jpg", "jpeg", "png", "svg"],)
                mode = "upload"

            elif option == "📷 **:blue[Take a photo]**":
                enable = st.checkbox("Enable camera")
                upload_img = st.camera_input(label="**:blue[Take a picture]**", disabled=not enable)
                mode = "camera"

            elif option == "🌐 **:blue[Load image from a URL]**":
                url = st.text_input("**:blue[Image URL]**", key="url")
                mode = "url"
                if url:
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            upload_img = Image.open(BytesIO(response.content))  # Directly set upload_img
                        else:
                            st.error("Failed to load image from URL.")
                    except Exception as e:
                        st.error(f"Error loading image: {e}")

            if upload_img is not None:

                if mode == "upload" or mode == "camera":
                    pil_img = Image.open(upload_img).convert("RGB")
                elif mode == "url":
                    pil_img = upload_img.convert("RGB")  # Since upload_img is already an Image object
                img_arr = np.asarray(pil_img)  # Convert PIL Image to NumPy array for display

                if mode == "upload":
                    file_details = {"File Name": upload_img.name,"File Size (KB)": round(upload_img.size / 1024, 2),
                    "Format": pil_img.format,"Mode": pil_img.mode,"Width (px)": pil_img.size[0],"Height (px)": pil_img.size[1],}
                else:
                    file_details = {"File Name": "Captured Image" if mode == "camera" else os.path.basename(url),
                    "File Size (KB)": "N/A","Format": pil_img.format,"Mode": pil_img.mode,"Width (px)": pil_img.size[0],"Height (px)": pil_img.size[1],}

                st.success("Image loaded successfully!")
                st.divider()
                conv_option = st.radio('Options', ['BW','Greyscale'], horizontal=True, label_visibility='collapsed', key='conv_option')
                
                if st.button("**Convert Image**"):
                    with col2:
                        with st.container(border=True):           
           
                            st.image(img_arr, use_container_width="auto", caption="Original Image")

                    with col3:
                        with st.container(border=True):                           
                    
                            if conv_option == "BW":
                                bw_img = pil_img.convert("1")  
                                st.image(bw_img, use_container_width="auto", caption="Black & White Image")
                                buffered = BytesIO()
                                bw_img.save(buffered, format="PNG")
                        
                            if conv_option == "Greyscale":
                                grey_img = pil_img.convert("L") 
                                st.image(grey_img, use_container_width="auto", caption="Greyscale Image")
                                buffered = BytesIO()
                                grey_img.save(buffered, format="PNG")

                        if conv_option == "BW":
                            st.download_button(label="**📥 Download Black & White Image**",data=buffered,file_name="black_white_image.png",mime="image/png",)
                                                            
                        if conv_option == "Greyscale":                                    
                            st.download_button(label="**📥 Download Greyscale Image**",data=buffered,file_name="greyscale_image.png",mime="image/png",)                       
 
            else:
                st.warning("Please upload/click/fetch a image file to convert.")

#---------------------------------------------------------------------------------------------------------------------------------
### Rotate
#---------------------------------------------------------------------------------------------------------------------------------

#with tab6:
#if page == "rotate":
elif st.session_state.page == 'img_rotate':

    st.markdown("---")      
    col_home, title= st.columns([2,15,])
            
    with col_home:
        if st.button("Home", icon="🏠", key="home_fd", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    with title:       
        st.info("""The **Rotate** tab is designed to rotate of the uploaded image files. You can upload or take photo using camera of load from a URL of an image and the tool will help to rotate of the image file.""")                     
    
    col1, col2, col3 = st.columns((0.15,0.45,0.4))
    with col1:
        with st.container(border=True):
            
            option = st.radio(
                label="Upload an image, take one with your camera, or load an image from a URL",
                options=(
                    "⬆️ **:blue[Upload an image]**",
                    "📷 **:blue[Take a photo]**",
                    "🌐 **:blue[Load image from a URL]**",),
                label_visibility="collapsed", help="Uploaded images are deleted from the server when you\n""* upload another image, or\n""* clear the file uploader, or\n""* close the browser tab",)

            st.divider()
            upload_img = None  # Ensure upload_img is always defined
            pil_img = None
            mode = None

            if option == "⬆️ **:blue[Upload an image]**":
                upload_img = st.file_uploader(label="**:blue[Upload an image]**",type=["bmp", "jpg", "jpeg", "png", "svg"],)
                mode = "upload"

            elif option == "📷 **:blue[Take a photo]**":
                enable = st.checkbox("Enable camera")
                upload_img = st.camera_input(label="**:blue[Take a picture]**", disabled=not enable)
                mode = "camera"

            elif option == "🌐 **:blue[Load image from a URL]**":
                url = st.text_input("**:blue[Image URL]**", key="url")
                mode = "url"
                if url:
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            upload_img = Image.open(BytesIO(response.content))  # Directly set upload_img
                        else:
                            st.error("Failed to load image from URL.")
                    except Exception as e:
                        st.error(f"Error loading image: {e}")

            if upload_img is not None:

                if mode == "upload" or mode == "camera":
                    pil_img = Image.open(upload_img).convert("RGB")
                elif mode == "url":
                    pil_img = upload_img.convert("RGB")  # Since upload_img is already an Image object
                img_arr = np.asarray(pil_img)  # Convert PIL Image to NumPy array for display

                if mode == "upload":
                    file_details = {"File Name": upload_img.name,"File Size (KB)": round(upload_img.size / 1024, 2),
                    "Format": pil_img.format,"Mode": pil_img.mode,"Width (px)": pil_img.size[0],"Height (px)": pil_img.size[1],}
                else:
                    file_details = {"File Name": "Captured Image" if mode == "camera" else os.path.basename(url),
                    "File Size (KB)": "N/A","Format": pil_img.format,"Mode": pil_img.mode,"Width (px)": pil_img.size[0],"Height (px)": pil_img.size[1],}

                st.success("Image loaded successfully!")
                st.divider()
                angle = st.slider("**Rotate**", min_value=0, max_value=360, value=0)
                
                if st.button("**Rotate Image**"):
                    with col2:
                        with st.container(border=True):           
           
                            st.image(img_arr, use_container_width="auto", caption="Original Image")

                    with col3:
                        with st.container(border=True):   
                                                    
                            rotated_img = pil_img.rotate(angle)
                            st.image(rotated_img, use_container_width="auto", caption=f"Rotated Image by {angle} degrees")
                            buffered = BytesIO()
                            rotated_img.save(buffered, format="PNG")
                        st.download_button(label="**📥 Download Rotated Image**",data=buffered,file_name="rotated_image.png",mime="image/png",)

            else:
                st.warning("Please upload/click/fetch a image file to rotate.")
                
#---------------------------------------------------------------------------------------------------------------------------------
### Change
#---------------------------------------------------------------------------------------------------------------------------------

#with tab7:
#if page == "change":
elif st.session_state.page == 'img_adjust':

    st.markdown("---")      
    col_home, title= st.columns([2,15,])
            
    with col_home:
        if st.button("Home", icon="🏠", key="home_fd", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    with title:       
        st.info("""The **Adjust** tab is designed to change the properties of the uploaded image files. You can upload or take photo using camera of load from a URL of an image and the tool will help to change the properties (e.g, brightness,saturation, sharpness, contrast) of the image file.""")                 
    
    col1, col2, col3 = st.columns((0.15,0.45,0.4))
    with col1:
        with st.container(border=True):
            
            option = st.radio(
                label="Upload an image, take one with your camera, or load an image from a URL",
                options=(
                    "⬆️ **:blue[Upload an image]**",
                    "📷 **:blue[Take a photo]**",
                    "🌐 **:blue[Load image from a URL]**",),
                label_visibility="collapsed", help="Uploaded images are deleted from the server when you\n""* upload another image, or\n""* clear the file uploader, or\n""* close the browser tab",)

            st.divider()
            upload_img = None  # Ensure upload_img is always defined
            pil_img = None
            mode = None

            if option == "⬆️ **:blue[Upload an image]**":
                upload_img = st.file_uploader(label="**:blue[Upload an image]**",type=["bmp", "jpg", "jpeg", "png", "svg"],)
                mode = "upload"

            elif option == "📷 **:blue[Take a photo]**":
                enable = st.checkbox("Enable camera")
                upload_img = st.camera_input(label="**:blue[Take a picture]**", disabled=not enable)
                mode = "camera"

            elif option == "🌐 **:blue[Load image from a URL]**":
                url = st.text_input("**:blue[Image URL]**", key="url")
                mode = "url"
                if url:
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            upload_img = Image.open(BytesIO(response.content))  # Directly set upload_img
                        else:
                            st.error("Failed to load image from URL.")
                    except Exception as e:
                        st.error(f"Error loading image: {e}")

            if upload_img is not None:

                if mode == "upload" or mode == "camera":
                    pil_img = Image.open(upload_img).convert("RGB")
                elif mode == "url":
                    pil_img = upload_img.convert("RGB")  # Since upload_img is already an Image object
                img_arr = np.asarray(pil_img)  # Convert PIL Image to NumPy array for display

                if mode == "upload":
                    file_details = {"File Name": upload_img.name,"File Size (KB)": round(upload_img.size / 1024, 2),
                    "Format": pil_img.format,"Mode": pil_img.mode,"Width (px)": pil_img.size[0],"Height (px)": pil_img.size[1],}
                else:
                    file_details = {"File Name": "Captured Image" if mode == "camera" else os.path.basename(url),
                    "File Size (KB)": "N/A","Format": pil_img.format,"Mode": pil_img.mode,"Width (px)": pil_img.size[0],"Height (px)": pil_img.size[1],}

                st.success("Image loaded successfully!")
                st.divider()
                stats_expander = st.expander("**:blue[Tuner]**", expanded=False)
                with stats_expander:
                        brightness = st.slider("**Brightness**", 0.0, 2.0, 1.0)
                        saturation = st.slider("**Saturation**", 0.0, 2.0, 1.0)
                        sharpness = st.slider("**Sharpness**", 0.0, 2.0, 1.0)
                        contrast = st.slider("**Contrast**", 0.0, 2.0, 1.0)
                
                if st.button("**Change Image**"):
                    with col2:
                        with st.container(border=True):           
           
                            st.image(img_arr, use_container_width="auto", caption="Original Image")

                    with col3:
                        with st.container(border=True):  

                            enhanced_img = ImageEnhance.Brightness(pil_img).enhance(brightness)
                            enhanced_img = ImageEnhance.Color(enhanced_img).enhance(saturation)
                            enhanced_img = ImageEnhance.Sharpness(enhanced_img).enhance(sharpness)
                            enhanced_img = ImageEnhance.Contrast(enhanced_img).enhance(contrast)
                            st.image(enhanced_img, use_container_width="auto", caption="Contrast Adjusted")
                            buffered = BytesIO()
                            enhanced_img.save(buffered, format="PNG")
                        st.download_button(label="**📥 Download Adjusted Image**",data=buffered,file_name="adjusted_image.png",mime="image/png",)

            else:
                st.warning("Please upload/click/fetch a image file to change.")
                
#---------------------------------------------------------------------------------------------------------------------------------
### Generate
#---------------------------------------------------------------------------------------------------------------------------------

#with tab8:
#if page == "generate":
elif st.session_state.page == 'img_generate':

    st.markdown("---")      
    col_home, title= st.columns([2,15,])
            
    with col_home:
        if st.button("Home", icon="🏠", key="home_fd", type="secondary", use_container_width=True):
            go_home()
            st.rerun()

    with title:       
        st.info("""The **Generate** tab is designed to generate new images based on the uploaded image files. You can upload or take photo using camera of load from a URL of an image and the tool will help to generate new images based on the the image file.""")   
    
    st.info('**Disclaimer : This portion is under Development**', icon="ℹ️") 
