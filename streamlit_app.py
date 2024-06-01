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

# Link to the respective pages using st.page_link
if menu_item == 'Home':
    st.page_link("pages/home.py", label="Home Page", icon="house-fill")
elif menu_item == 'Apple':
    st.page_link("pages/apple.py", label="Apple Page", icon="apple")
elif menu_item == 'Google':
    st.page_link("pages/google.py", label="Google Page", icon="google")
elif menu_item == 'Products':
    st.page_link("pages/products.py", label="Products Page", icon="box-fill")

st.sidebar.write("Menu item selected: ", menu_item)
