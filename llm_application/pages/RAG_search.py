import pickle
import streamlit as st
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from pages.lib.openai_call import get_embedding, get_chat_openai
from pages.lib.prompts import SEARCH_PROMPT


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

sentence = st.text_input("질문을 입력하세요")
if st.button("답변 생성"):
    query_embedding = get_embedding(sentence)
    with open("paragraphs.pickle", "rb") as f:
        total_data = pickle.load(f)

    paragraph = total_data["paragraph"]
    context_embedding = total_data["openai_embedding"]

    query_embedding = np.array(query_embedding)
    context_embedding = np.array(context_embedding)

    similarity_scores = cosine_similarity([query_embedding], context_embedding)
    max_index = np.argmax(similarity_scores)

    context = paragraph[max_index]

    prompt = SEARCH_PROMPT.format(context=context, question=sentence)
    answer = get_chat_openai(prompt)

    st.markdown("### 마크다운")
    st.write(prompt)
    st.markdown("### 답변")
    st.write(answer)
