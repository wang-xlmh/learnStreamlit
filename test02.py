import streamlit as st
import base64


# 使用缓存装饰器来避免重复加载图片
@st.cache_data(ttl="1d")
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_jpg_as_page_bg(jpg_file, opacity=0.7):
    bin_str = get_base64_of_bin_file(jpg_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        opacity: {opacity};
    }}
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)


# 假设 'background.jpg' 是与你的 Streamlit 脚本在同一目录下的图片文件
set_jpg_as_page_bg('static/image/background04.jpg', opacity=0.7)

# 添加其他 Streamlit 代码来创建你的应用程序
st.title('My Streamlit App with Background Image')
st.write('This is the main content of the app.')