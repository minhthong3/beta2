import streamlit as st
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def Google():
    st.title('Welcome to apple google!!')

# Cấu hình xác thực
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("image/datavnwealth-937493720206.json", scope)
client = gspread.authorize(creds)

# URL của Google Sheets
sheet_url = "https://docs.google.com/spreadsheets/d/1kkOjUihnNpcWn8jmNM7majctXlqU18fGvwlTOVi9efg/edit#gid=0"

# Đọc dữ liệu từ Google Sheets
def load_data():
    sheet = client.open_by_url(sheet_url).sheet1
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    return df

# Hiển thị dữ liệu với CSS
def display_with_css(df):
    st.markdown(
        f"""
        <style>
        .scrollable-table-container {{
            max-height: 400px;  /* Chiều cao cố định cho bảng */
            overflow-y: auto;  /* Cho phép cuộn theo chiều dọc */
            background-color: white;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
            border: 1px solid #ddd;  /* Đường viền cho bảng */
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th {{
            background-color: orange;  /* Nền màu cam cho tiêu đề */
            color: white;  /* Chữ màu trắng */
            text-align: center;  /* Văn bản căn giữa */
            border: 1px solid white;  /* Đường viền màu trắng */
        }}
        td {{
            background-color: white;  /* Nền màu trắng */
            border: 1px solid #ddd;  /* Đường viền màu xám nhạt */
            padding: 8px;
            text-align: left;
        }}
        .tin_hieu {{
            color: black;
        }}
        .tin_hieu[data-value="MUA"] {{
            color: green;  /* Màu xanh lá cây cho "MUA" */
        }}
        .tin_hieu[data-value="BÁN"] {{
            color: red;  /* Màu đỏ cho "BÁN" */
        }}
        .gia_hien_tai {{
            color: black;
        }}
        .gia_hien_tai[data-percent-value^="-"] {{
            color: red;  /* Màu đỏ cho giá trị âm */
        }}
        .gia_hien_tai[data-percent-value="0.0"] {{
            color: orange;  /* Màu vàng cho giá trị bằng 0 */
        }}
        .gia_hien_tai[data-percent-value="0"] {{
            color: orange;  /* Màu vàng cho giá trị bằng 0 */
        }}
        .gia_hien_tai[data-percent-value="0.00"] {{
            color: orange;  /* Màu vàng cho giá trị bằng 0 */
        }}
        .gia_hien_tai[data-percent-value]:not([data-percent-value^="-"]):not([data-percent-value="0"]):not([data-percent-value="0.0"]):not([data-percent-value="0.00"]) {{
            color: green;  /* Màu xanh lá cây cho giá trị dương */
        }}
        .percent {{
            color: black;
        }}
        .percent[data-value^="-"] {{
            color: red;  /* Màu đỏ cho giá trị âm */
        }}
        .percent[data-value="0.0"] {{
            color: orange;  /* Màu vàng cho giá trị bằng 0 */
        }}
        .percent[data-value="0"] {{
            color: orange;  /* Màu vàng cho giá trị bằng 0 */
        }}
        .percent[data-value="0.00"] {{
            color: orange;  /* Màu vàng cho giá trị bằng 0 */
        }}
        .percent[data-value]:not([data-value^="-"]):not([data-value="0"]):not([data-value="0.0"]):not([data-value="0.00"]) {{
            color: green;  /* Màu xanh lá cây cho giá trị dương */
        }}
        </style>
        """, unsafe_allow_html=True
    )

    def format_value(val, class_name):
        if pd.isna(val):
            return f'<td class="{class_name}" data-value=""></td>'
        return f'<td class="{class_name}" data-value="{val}">{val}</td>'

    def format_row(row):
        try:
            percent_value = row["pct_change"]
        except KeyError:
            percent_value = 0  # Hoặc giá trị mặc định nào đó

        gia_hien_tai_color_class = ""
        if percent_value > 0:
            gia_hien_tai_color_class = "gia_hien_tai"
        elif percent_value < 0:
            gia_hien_tai_color_class = "gia_hien_tai"
        else:
            gia_hien_tai_color_class = "gia_hien_tai"
        
        return [
            f'<td>{row["Mã"]}</td>',
            format_value(row.get("Tín hiệu", ""), "tin_hieu"),  # Sử dụng get để tránh lỗi KeyError
            f'<td class="{gia_hien_tai_color_class}" data-percent-value="{percent_value}">{row.get("Giá hiện tại", "")}</td>',
            f'<td class="percent" data-value="{percent_value}">{percent_value}</td>'
        ]

    # Lọc dữ liệu để chỉ hiển thị các dòng có giá trị trong cột "Tín hiệu"
    df_filtered = df[df["Tín hiệu"].notnull() & df["Tín hiệu"].str.strip().ne("")]

    formatted_rows = [format_row(row) for _, row in df_filtered.iterrows()]
    html = "<div class='scrollable-table-container'><table class='dataframe'>"
    html += "<thead><tr><th>Mã</th><th>Tín hiệu</th><th>Giá hiện tại</th><th>pct_change</th></tr></thead>"
    html += "<tbody>"
    for row in formatted_rows:
        html += "<tr>" + "".join(row) + "</tr>"
    html += "</tbody></table></div>"

    st.markdown(html, unsafe_allow_html=True)

def main():
    # Cấu hình trang web với chế độ wide mode
    st.set_page_config(layout="wide")
    
    st.title("Flash Deal - Mua Nhanh - Chốt lời lẹ")
    st.write("Tín hiệu khuyến nghị của Flash Deal dựa trên Chiến lược Đầu tư Kỹ thuật")  
    st.write("Tín hiệu khuyến nghị thời gian thực - Dữ liệu được cập nhật 10 giây một lần từ 9h15 đến 15h00")  

    data = load_data()
    
    display_with_css(data)
    
    # Tự động làm mới trang sau mỗi 10 giây
    st_autorefresh(interval=10 * 1000)

if __name__ == "__main__":
    main()
