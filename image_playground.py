import streamlit as st
import numpy as np
from PIL import Image, ImageDraw
from skimage import color, filters, measure, morphology, draw

def process_image(image):
    # Convert image to grayscale
    gray_image = color.rgb2gray(image)
    
    # Apply Gaussian filter to reduce noise
    blurred_image = filters.gaussian(gray_image, sigma=2.0)
    
    # Apply Otsu's thresholding
    thresh = filters.threshold_otsu(blurred_image)
    binary_image = blurred_image < thresh
    
    # Remove small objects and noise
    cleaned_image = morphology.remove_small_objects(binary_image, min_size=100)
    
    # Label the connected regions in the binary image
    labeled_image = measure.label(cleaned_image)
    
    return labeled_image

def calculate_diameters(labeled_image):
    diameters = []
    properties = measure.regionprops(labeled_image)
    for prop in properties:
        # Calculate the equivalent diameter
        diameter = prop.equivalent_diameter
        diameters.append(diameter)
    return diameters, properties

def draw_contours(image, properties, diameters):
    output = Image.fromarray(image)
    draw_output = ImageDraw.Draw(output)
    for prop, diameter in zip(properties, diameters):
        y, x = prop.centroid
        radius = diameter / 2
        
        # Get the coordinates of the circle's perimeter
        rr, cc = draw.circle_perimeter(int(y), int(x), int(radius), shape=image.shape)
        
        # Draw the circle perimeter
        for r, c in zip(rr, cc):
            if 0 <= r < image.shape[0] and 0 <= c < image.shape[1]:
                output.putpixel((c, r), (0, 255, 0))  # Green circle

        # Draw the diameter text
        draw_output.text((x - 20, y - 20), f'{int(diameter)}px', fill=(255, 0, 0))  # Red text
    
    return output

def main():
    st.title("Molecule Counter and Diameter Measurement")

    uploaded_file = st.file_uploader("Upload an image of molecules", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load the image
        image = np.array(Image.open(uploaded_file))
        
        # Process the image to find contours
        labeled_image = process_image(image)
        
        # Calculate diameters of the molecules
        diameters, properties = calculate_diameters(labeled_image)
        
        # Draw contours and diameters on the image
        output_image = draw_contours(image, properties, diameters)
        
        # Display the results
        st.image(output_image, caption=f"Detected Molecules: {len(diameters)}", use_column_width=True)
        
        # Display diameters
        st.write("Diameters of detected molecules (in pixels):")
        st.write(diameters)

if __name__ == "__main__":
    main()
