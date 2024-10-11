import streamlit as st
import base64
import os

# 获取当前脚本所在目录的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))

# 图片文件的绝对路径
image_path = os.path.abspath(os.path.join(script_dir, 'static', 'image', 'background04.jpg'))

# 检查文件是否存在
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# 加载图片并转换为 base64
def load_image_as_base64(file_path):
    with open(file_path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode()

base64_image = load_image_as_base64(image_path)

# 设置页面背景图片，并调节透明度
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
  position: relative;
  background-image: url("data:image/jpeg;base64,{base64_image}");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-color: rgba(255, 255, 255, 0.3); /* 背景颜色，透明度为 0.3 */
  background-blend-mode: overlay; /* 混合模式 */
}}

/* 包裹主要内容的透明容器 */
.content-container {{
  background-color: rgba(255, 255, 255, 0.9); /* 主要内容区域的透明度 */
  padding: 20px;
  border-radius: 10px;
  margin: 20px;
  z-index: 1;
  position: relative;
}}
</style>
"""

# 创建完整的 HTML 结构来确保内容被正确包裹
html_content = f"""
<body>
<div class="content-container">
  <h1>My Streamlit App with Background Image</h1>
  <p>This is the main content of the app.</p>
</div>
</body>
"""

# 应用背景图片
st.markdown(page_bg_img, unsafe_allow_html=True)

# 包裹主要内容的透明容器
st.markdown(html_content, unsafe_allow_html=True)