import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import numpy as np
import yaml
from yaml.loader import SafeLoader
from streamlit_quill import st_quill
st.set_page_config(layout="wide")

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
df1 = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
df2 = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
# hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

col_title, col_contents = st.columns([1, 11])
with col_title:
    st.header(":red[LOGO]")
with col_contents:
    tab_home, tab_cell, tab_data, tab_protocol, tab_labnote, tab_stock, tab_mypage = st.tabs(["Home", "Cell", "Data", "Protocol", "Lab Note", "Stock", "My Page"])
    with tab_home:
        print("tab_home")
    with tab_cell:
        print("tab_cell")
    with tab_data:
        print("tab_data")
    with tab_protocol:
        print("tab_protocol")
    with tab_labnote:
        tab_labnote_col_left, tab_labnote_col_center, tab_labnote_col_right = st.columns([1,1,1])
        with tab_labnote_col_left:
            # st.header("◀")
            pass
        with tab_labnote_col_center:
            st.date_input("", value="today")
        with tab_labnote_col_right:
            # st.header("▶")
            pass
        tab_labnote_main_content = st.container()
        tab_labnote_active_cell_line = st.container()
        tab_labnote_active_cell_line.header("Active Cell Line")
        tab_labnote_active_cell_line_tab1, tab_labnote_active_cell_line_tab2 = st.tabs(["PSC", "mDA"])
        with tab_labnote_active_cell_line_tab1:
            st.table(df1)
        with tab_labnote_active_cell_line_tab2:
            st.table(df2)
        tab_labnote_note = st.container()
        tab_labnote_note.header("Note")
        tab_labnote_note_texteditor = st_quill()
        tab_labnote_note_texteditor
        print("tab_labnote")
    with tab_stock:
        print("tab_stock")
    with tab_mypage:
        print("tab_mypage")
        name, authentication_status, username = authenticator.login('Login', 'main')