import streamlit as st

# Dummy user credentials for login
USERNAME = "user"
PASSWORD = "pass"

# Initialize session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Function to display the login form
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password")

# Function to display the main app after successful login
def main_app():
    st.sidebar.button("Sign Out", on_click=sign_out)
    
    tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
    
    with tab1:
        st.header("Welcome to Tab 1")
        # Add your tab 1 content here
        
    with tab2:
        st.header("Welcome to Tab 2")
        # Add your tab 2 content here

    with tab3:
        st.header("Welcome to Tab 3")
        # Add your tab 3 content here

# Function to handle sign out
def sign_out():
    st.session_state.logged_in = False
    st.experimental_rerun()

# Main app logic
if st.session_state.logged_in:
    main_app()
else:
    login()
