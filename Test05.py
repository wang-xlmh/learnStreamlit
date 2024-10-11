import streamlit as st
import base64
import os
from datetime import datetime

# 设置页面配置
st.set_page_config(page_title="AI问答助手", page_icon="🤖", layout="wide")

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
</style>
"""

# 应用背景图片
st.markdown(page_bg_img, unsafe_allow_html=True)

# 设置页面标题
st.title("🤖 AI问答助手")

# 初始化对话记录
user_avator = "🧑‍💻"
robot_avator = "🤖"

if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示头部信息
st.header("模拟对话")

# 使用 chat_input 和 chat_message 构建聊天界面
col1, col2 = st.columns([5, 3])

# 显示历史消息
with col1:
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=message.get("avatar")):
            st.markdown(message["content"])

def add_message(role, content, avatar):
    """Add a new message to the chat history."""
    with st.chat_message(role, avatar=avatar):
        st.markdown(content)
    st.session_state.messages.append({"role": role, "content": content, "avatar": avatar})

# 用户输入
if user_query := st.chat_input("请输入内容..."):
    # 显示用户的输入
    add_message("user", user_query, user_avator)

    # 模拟机器人的响应
    simulated_response = f"这是对问题 '{user_query}' 的模拟响应。"

    # 显示机器人的响应
    add_message("robot", simulated_response, robot_avator)

# 自动滚动到最新消息
st.markdown("""
    <script>
    setTimeout(function() {
        var element = document.querySelector('.stVertical div[data-testid="stVerticalBlock"] > div:last-child .stChatMessages');
        if (element) {
            element.scrollTop = element.scrollHeight - element.offsetHeight;
        }
    }, 100);
    </script>
    """, unsafe_allow_html=True)