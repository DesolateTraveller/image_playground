import streamlit as st
import cv2
import numpy as np
from PIL import Image

def process_image(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian Blur to reduce noise and improve contour detection
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    
    # Apply thresholding to create a binary image
    _, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours of the molecules
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    return contours

def calculate_diameters(contours):
    diameters = []
    for contour in contours:
        # Calculate the enclosing circle diameter
        (x, y), radius = cv2.minEnclosingCircle(contour)
        diameter = 2 * radius
        diameters.append(diameter)
    return diameters

def draw_contours(image, contours, diameters):
    output = image.copy()
    for contour, diameter in zip(contours, diameters):
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)
        cv2.circle(output, center, radius, (0, 255, 0), 2)
        cv2.putText(output, f'{int(diameter)}px', (center[0] - 20, center[1] - 20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    return output

def main():
    st.title("Molecule Counter and Diameter Measurement")

    uploaded_file = st.file_uploader("Upload an image of molecules", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load the image
        image = np.array(Image.open(uploaded_file))
        
        # Process the image to find contours
        contours = process_image(image)
        
        # Calculate diameters of the molecules
        diameters = calculate_diameters(contours)
        
        # Draw contours and diameters on the image
        output_image = draw_contours(image, contours, diameters)
        
        # Display the results
        st.image(output_image, caption=f"Detected Molecules: {len(contours)}", use_column_width=True)
        
        # Display diameters
        st.write("Diameters of detected molecules (in pixels):")
        st.write(diameters)

if __name__ == "__main__":
    main()
