import streamlit as st
from streamlit_navigation_bar import st_navbar
import streamlit_antd_components as sac
import toml

# Đọc cấu hình trang từ file pages.toml
def load_pages():
    with open("pages.toml", "r") as f:
        return toml.load(f)["pages"]

pages = load_pages()

# Đặt các giá trị mặc định cho session_state nếu chưa có
if 'menu_item' not in st.session_state:
    st.session_state['menu_item'] = 'home'

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

    match menu_item:
        case 'apple':
            st.session_state['menu_item'] = 'apple'
        case 'google':
            st.session_state['menu_item'] = 'google'

# Hiển thị trang được chọn
for page in pages:
    if page["id"] == st.session_state['menu_item'] and not page.get("disabled", False):
        exec(open(page["file"]).read())
        break
