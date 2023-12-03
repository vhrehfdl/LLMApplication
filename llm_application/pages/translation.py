import streamlit as st
from pages.lib.prompts import TRANSLATE_PROMPT
from pages.lib.openai_call import get_chat_openai

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# 텍스트 입력 받기
sentence = st.text_input("번역하고 싶은 문장을 입력하세요")
language = st.radio("언어를 선택해주세요", ("한국어", "English", "日本語"))

if st.button("번역"):
    prompt = TRANSLATE_PROMPT.format(text=sentence, language=language)
    result_summary = get_chat_openai(prompt)
    st.write(result_summary)
