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
        sac.MenuItem('Home', icon='house-fill', href='?page=home'),
        sac.MenuItem('Products', icon='box-fill', children=[
            sac.MenuItem('Apple', icon='apple', href='?page=apple'),
            sac.MenuItem('Google', icon='google', href='?page=google'),
        ]),
    ], open_all=True)

# Lấy giá trị của tham số 'page' từ URL
page = st.experimental_get_query_params().get('page', ['home'])[0]

# Chuyển hướng theo giá trị của 'page'
if page == 'home':
    exec(open('pages/home.py').read(), globals())
elif page == 'apple':
    exec(open('pages/apple.py').read(), globals())
elif page == 'google':
    exec(open('pages/google.py').read(), globals())
elif page == 'products':
    exec(open('pages/products.py').read(), globals())
else:
    st.error("Page not found")


