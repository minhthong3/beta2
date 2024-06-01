import streamlit as st
import streamlit_antd_components as sac

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

# Chuyển hướng theo menu item được chọn
if menu_item == 'Home':
     st.switch_page('pages/home.py')
elif menu_item == 'Apple':
   st.switch_page('pages/apple.py')
elif menu_item == 'Google':
    st.switch_page('pages/google.py')
elif menu_item == 'Products':
    st.switch_page('pages/products.py')


