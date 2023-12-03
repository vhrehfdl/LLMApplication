import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

markdown = """
# LLM Web Application Tutorial
## Pages
1. simple streamlit : streamlit input & output 테스트
2. simple api call : 문장과 언어를 입력하면 해당 언어로 변환
"""

st.markdown(markdown)
