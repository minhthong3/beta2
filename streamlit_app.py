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
    exec(open('pages/home.py').read())
elif menu_item == 'Apple':
    st.page_link ('pages/apple.py')
elif menu_item == 'Google':
    exec(open('pages/google.py').read())
elif menu_item == 'Products':
    exec(open('pages/products.py').read())

st.sidebar.write("Menu item selected: ", menu_item)
