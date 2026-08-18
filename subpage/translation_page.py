import streamlit as st

from tools.translation import (
    translate_en_to_cn,
    translate_cn_to_en,
)


def show_translation_page():

    st.header("中英互译")

    text = st.text_area("文本")

    direction = st.radio(
        "翻译方向",
        [
            "中文 → English",
            "English → 中文",
        ]
    )

    if st.button("翻译"):

        if not text:
            st.warning("请输入翻译文本")

        else:
            with st.spinner("正在翻译..."):

                if direction == "中文 → English":
                    result = translate_cn_to_en(
                        text=text
                    )
                else:
                    result = translate_en_to_cn(
                        text=text
                    )

            st.subheader("生成译文")
            st.write(result)