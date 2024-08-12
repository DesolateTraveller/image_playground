import streamlit as st

# Define sign out function
def sign_out():
    st.session_state.logged_in = False
    st.experimental_set_query_params(logged_in="false")

# Check if user is logged in
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Page configuration
st.set_page_config(page_title="PDF Playground | v0.1",
                    layout="wide",
                    page_icon="📘",            
                    initial_sidebar_state="collapsed")

# If not logged in, show the login page
if not st.session_state.logged_in:
    # Two columns for login page
    col1, col2 = st.columns(2)

    with col1:
        st.title(f""":rainbow[PDF Playground]""")
        st.markdown(
            '''
            Created by | <a href="mailto:avijit.mba18@gmail.com">Avijit Chakraborty</a> |
            for best view of the app, please **zoom-out** the browser to **75%**.
            ''',
            unsafe_allow_html=True)
        st.info('**An easy-to-use, open-source PDF application to preview and extract content and metadata from PDFs, add or remove passwords, modify, merge, convert and compress PDFs**', icon="ℹ️")
    
    with col2:
        st.subheader("Login to Access PDF Playground")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == "admin" and password == "password":  # Simplified for example purposes
                st.session_state.logged_in = True
                st.experimental_set_query_params(logged_in="true")
            else:
                st.error("Invalid username or password")

# If logged in, show the main app
if st.session_state.logged_in:
    # Sign out button on the top right
    st.sidebar.button("Sign Out", on_click=sign_out)
    
    # Main app content
    st.title(f""":rainbow[PDF Playground]""")
    st.markdown(
        '''
        Created by | <a href="mailto:avijit.mba18@gmail.com">Avijit Chakraborty</a> |
        for best view of the app, please **zoom-out** the browser to **75%**.
        ''',
        unsafe_allow_html=True)
    st.info('**An easy-to-use, open-source PDF application to preview and extract content and metadata from PDFs, add or remove passwords, modify, merge, convert and compress PDFs**', icon="ℹ️")

    # (Add your main app's tabs and functionality here)
