import streamlit as st
from dotenv import load_dotenv

from subpage.copywriting_page import show_copywriting_page
from subpage.translation_page import show_translation_page
from subpage.pdf_page import show_pdf_page

load_dotenv()

st.title("AI Assistant")

page = st.sidebar.radio(
    "功能",
    [
        "文案生成",
        "中英翻译",
        "PDF内容处理"
    ]
)

if page == "文案生成":
    show_copywriting_page()

elif page == "中英翻译":
    show_translation_page()

elif page == "PDF内容处理":
    show_pdf_page()