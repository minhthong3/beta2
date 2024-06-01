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
        sac.MenuItem('home', icon='house-fill', tag=[sac.Tag('Tag1', color='green'), sac.Tag('Tag2', 'red')]),
        sac.MenuItem('products', icon='box-fill', children=[
            sac.MenuItem('apple', icon='apple'),
            sac.MenuItem('other', icon='git', description='other items', children=[
                sac.MenuItem('google', icon='google', description='item description'),
                sac.MenuItem('gitlab', icon='gitlab'),
                sac.MenuItem('wechat', icon='wechat'),
            ]),
        ]),
        sac.MenuItem('disabled', disabled=True),
        sac.MenuItem(type='divider'),
        sac.MenuItem('link', type='group', children=[
            sac.MenuItem('antd-menu', icon='heart-fill', href='https://ant.design/components/menu#menu'),
            sac.MenuItem('bootstrap-icon', icon='bootstrap-fill', href='https://icons.getbootstrap.com/'),
        ]),
    ], open_all=True)

    # Chuyển hướng theo menu item được chọn
    if menu_item == 'home':
        exec(open('pages/home.py').read(), globals())
    elif menu_item == 'apple':
        exec(open('pages/apple.py').read(), globals())
    elif menu_item == 'google':
        exec(open('pages/google.py').read(), globals())
    elif menu_item == 'products':
        exec(open('pages/products.py').read(), globals())

st.sidebar.write("Menu item selected: ", menu_item)
