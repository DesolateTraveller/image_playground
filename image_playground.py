import streamlit as st

# Function to center content vertically
def center_content():
    st.write(
        """
        <style>
        .centered {
            display: flex;
            flex-direction: column;
            justify-content: center;
            height: 100vh;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Sign-out function
def sign_out():
    st.session_state.logged_in = False
    st.experimental_set_query_params(logged_in="false")

# Function to authenticate user
def authenticate(username, password):
    # Simplified authentication logic
    if username == "user" and password == "password":
        return True
    return False

# Page configuration
st.set_page_config(page_title="PDF Playground | v0.1",
                   layout="wide",
                   page_icon="📘",
                   initial_sidebar_state="collapsed")

# Check if user is logged in
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Display login page if not logged in
if not st.session_state.logged_in:
    center_content()

    with st.container():
        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown(
                '''
                <div class="centered">
                <h1 style='text-align: center; color: #FF6347;'>PDF Playground</h1>
                <p style='text-align: center;'>An easy-to-use, open-source PDF application to preview and extract content and metadata from PDFs, add or remove passwords, modify, merge, convert and compress PDFs.</p>
                <p style='text-align: center;'>Created by <a href="mailto:avijit.mba18@gmail.com">Avijit Chakraborty</a></p>
                <p style='text-align: center;'>For best view of the app, please zoom-out the browser to 75%.</p>
                </div>
                ''',
                unsafe_allow_html=True
            )

        with col2:
            st.markdown("<div class='centered'>", unsafe_allow_html=True)

            st.subheader("Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login_button = st.button("Login")

            if login_button:
                if authenticate(username, password):
                    st.session_state.logged_in = True
                    st.experimental_set_query_params(logged_in="true")
                    st.experimental_rerun()  # Rerun to access the main page immediately
                else:
                    st.error("Invalid username or password")

            st.markdown("</div>", unsafe_allow_html=True)
else:
    # Main app content
    st.title(":rainbow[PDF Playground]")
    st.markdown(
        '''
        Created by | <a href="mailto:avijit.mba18@gmail.com">Avijit Chakraborty</a> |
        for best view of the app, please **zoom-out** the browser to **75%**.
        ''',
        unsafe_allow_html=True)
    st.info('**An easy-to-use, open-source PDF application to preview and extract content and metadata from PDFs, add or remove passwords, modify, merge, convert and compress PDFs**', icon="ℹ️")

    # Sign-out button at the top right
    st.markdown(
        """
        <style>
        .logout-button {
            position: absolute;
            top: 10px;
            right: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.button("Sign Out", key="signout", on_click=sign_out):
        st.experimental_rerun()
