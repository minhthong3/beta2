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

match menu_item:
    case 'Home':
        st.write("Home Page")
        exec(open('pages/home.py').read(), globals())
    case 'Apple':
        st.write("Apple Page")
        exec(open('pages/apple.py').read(), globals())
    case 'Google':
        st.write("Google Page")
        exec(open('pages/google.py').read(), globals())
    case 'Products':
        st.write("Products Page")
        exec(open('pages/products.py').read(), globals())

st.sidebar.write("Menu item selected: ", menu_item)
