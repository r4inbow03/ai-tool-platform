import streamlit as st

from tools.pdf import extract_pdf_text
from tools.summary import ai_summary
from tools.rag_chatbot import rag_query, initialize_rag

def show_pdf_page():

    st.header("PDF处理")

    file = st.file_uploader(
        "上传PDF文件",
        type=["pdf"]
    )

    if file is None:
        st.info("请先上传PDF文件")
        return

    st.success(f"已上传：{file.name}")

    text = extract_pdf_text(file)

    if not text:
        st.error("无法从该PDF中提取文本")
        return

    direction = st.radio(
        "功能",
        [
            "AI摘要总结",
            "自行提问",
        ],
        horizontal=True
    )

    if direction == "AI摘要总结":

        if st.button("生成总结"):
            with st.spinner("正在生成总结..."):
                result = ai_summary(text)
                st.subheader("ai摘要：")
                st.write(result)

    else:

        question = st.text_input(
            "请输入你的问题",
            placeholder="例如：这篇PDF的主要内容是什么？"
        )

        if st.button("生成回复"):
            if not question.strip():
                st.warning("请输入问题")
            else:
                with st.spinner("正在生成回复..."):
                    chunks = initialize_rag(text)
                    answer = rag_query(
                        question,
                        chunks,
                    )

                    st.write(answer)