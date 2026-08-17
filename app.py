import streamlit as st
from dotenv import load_dotenv

from tools.copywriting import generate_copywriting

# 加载 .env
load_dotenv()

st.title("AI 文案生成器")

product = st.text_input("产品")
target_audience = st.text_input("目标用户")

style = st.selectbox(
    "文案风格",
    ["专业", "简洁", "活泼", "高端"]
)

if st.button("生成文案"):

    if not product:
        st.warning("请输入产品信息")
    if not target_audience:
        st.warning("请输入目标用户")
    else:
        with st.spinner("正在生成..."):
            result = generate_copywriting(
                product=product,
                target_audience=target_audience,
                style=style
            )

        st.subheader("生成结果")
        st.write(result)