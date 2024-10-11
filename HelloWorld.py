import streamlit as st
import base64


# 使用缓存装饰器来避免重复加载图片
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_jpg_as_page_bg(jpg_file):
    bin_str = get_base64_of_bin_file(jpg_file)
    page_bg_img = '''
    <style>
    body { 
    background-image: url("data:image/jpeg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


# 假设 'background01.jpg' 是与你的 Streamlit 脚本在同一目录下的图片文件
set_jpg_as_page_bg('static/image/background01.jpg')

# 添加其他 Streamlit 代码来创建你的应用程序
st.title('My Streamlit App with Background Image')