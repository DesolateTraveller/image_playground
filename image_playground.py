import streamlit as st

#---------------------------------------------------------------------------------------------------------------------------------
### Title and description for your Streamlit app
#---------------------------------------------------------------------------------------------------------------------------------
st.set_page_config(page_title="PDF Playground | v0.1",
                    layout="wide",
                    page_icon="📘",            
                    initial_sidebar_state="collapsed")

#---------------------------------------------------------------------------------------------------------------------------------
### Authentication Functionality
#---------------------------------------------------------------------------------------------------------------------------------
def login():
    st.session_state['logged_in'] = True

def logout():
    st.session_state['logged_in'] = False

def show_login_page():
    st.markdown("### Please log in to access the app")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":  # Replace with your own validation logic
            login()
        else:
            st.error("Incorrect username or password")

def show_logout_button():
    if st.button("Logout"):
        logout()

#---------------------------------------------------------------------------------------------------------------------------------
### Main App Content
#---------------------------------------------------------------------------------------------------------------------------------
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    show_login_page()
else:
    show_logout_button()
    
    # Main App Content
    st.title(f""":rainbow[PDF Playground]""")

    st.markdown(
        '''
        Created by | <a href="mailto:avijit.mba18@gmail.com">Avijit Chakraborty</a> |
        for best view of the app, please **zoom-out** the browser to **75%**.
        ''',
        unsafe_allow_html=True
    )

    st.info('''
        **An easy-to-use, open-source PDF application to preview and extract content and metadata from PDFs, 
        add or remove passwords, modify, merge, convert, and compress PDFs.**
    ''', icon="ℹ️")

    st.markdown(
        '''
        ---
        ## **App Features:**
        - **Preview** PDF files
        - **Extract** text and images
        - **Merge** multiple PDFs
        - **Compress** PDF files
        - **Protect/Unlock** PDFs
        - **Convert** PDFs to Word documents
        - **Rotate/Resize** PDFs

        ---
        '''
    )

    st.sidebar.markdown("### PDF Playground | v0.1 Navigation")
    st.sidebar.markdown("[Home](#)")
    st.sidebar.markdown("[Preview PDFs](#preview)")
    st.sidebar.markdown("[Extract Content](#extract)")
    st.sidebar.markdown("[Merge PDFs](#merge)")
    st.sidebar.markdown("[Compress PDFs](#compress)")
    st.sidebar.markdown("[Protect/Unlock PDFs](#protect-unlock)")
    st.sidebar.markdown("[Convert to Word](#convert)")
    st.sidebar.markdown("[Rotate/Resize PDFs](#rotate-resize)")

