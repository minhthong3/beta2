import streamlit as st
import streamlit_antd_components as sac
from pages.apple import Apple
from pages.home import Home
from pages.products import Products
from pages.google import Google

# CSS để ẩn sidebar mặc định
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

# Tạo menu trong sidebar
with st.sidebar:
    menu_item = sac.menu([
        sac.MenuItem('Home', icon='house-fill'),
        sac.MenuItem('Products', icon='box-fill', children=[
            sac.MenuItem('Apple', icon='apple'),
            sac.MenuItem('Google', icon='google'),
        ]),
    ], open_all=True)

match menu_item:
    case 'Home':
        st.switch_page('pages/home.py')
    case 'Apple':
        st.switch_page('pages/apple.py')
    case 'Google':
        st.switch_page('pages/google.py')
     case 'Products':
        st.switch_page('pages/products.py')

