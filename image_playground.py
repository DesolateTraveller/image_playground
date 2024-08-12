import streamlit as st

# Page configuration
st.set_page_config(
    page_title="PDF Playground | v0.1",
    layout="wide",
    page_icon="📘",
    initial_sidebar_state="collapsed"
)

# Session state initialization
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

def authenticate(username, password):
    # Replace these credentials with your own authentication logic
    return username == "admin" and password == "password"

def logout():
    st.session_state['authenticated'] = False

# Login page
def login_page():
    st.markdown("<h2 style='text-align: center;'>🔒 Login to PDF Playground</h2>", unsafe_allow_html=True)
    with st.form(key='login_form', clear_on_submit=True):
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        submit_button = st.form_submit_button('Login')
        
        if submit_button:
            if authenticate(username, password):
                st.session_state['authenticated'] = True
                st.experimental_rerun()
            else:
                st.error("Invalid credentials. Please try again.")

# Main app page
def main_page():
    # Sign-out button at the top right corner
    st.markdown(
        """
        <style>
        .logout-button {
            position: absolute;
            right: 10px;
            top: 10px;
            border-radius: 5px;
            background-color: #f44336;
            color: white;
            padding: 5px 10px;
            text-decoration: none;
            font-size: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown('<a href="#" class="logout-button" onClick="logout()">Sign Out</a>', unsafe_allow_html=True)

    st.title(f""":rainbow[PDF Playground]""")
    st.markdown(
        '''
        Created by | <a href="mailto:avijit.mba18@gmail.com">Avijit Chakraborty</a> |
        for best view of the app, please **zoom-out** the browser to **75%**.
        ''',
        unsafe_allow_html=True
    )
    st.info('**An easy-to-use, open-source PDF application to preview and extract content and metadata from PDFs, add or remove passwords, modify, merge, convert and compress PDFs**', icon="ℹ️")

if st.session_state['authenticated']:
    main_page()
else:
    login_page()
