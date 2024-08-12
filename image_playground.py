import streamlit as st

# User credentials for the login
USERNAME = "user"
PASSWORD = "pass"

# Function to verify login credentials
def verify_login(username, password):
    return username == USERNAME and password == PASSWORD

# Streamlit app configuration
st.set_page_config(page_title="Login App", layout="centered")

# Title of the app
st.title("Streamlit Login Form")

# Login form
st.subheader("Please log in to access the app")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Login button
if st.button("Login"):
    if verify_login(username, password):
        st.success("Login successful!")
        st.write("Welcome to the app!")
        # Here you can add the rest of your app's code or navigate to a different page
    else:
        st.error("Invalid username or password")
