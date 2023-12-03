import pickle
import pdfplumber
import streamlit as st
from pages.lib.openai_call import get_embedding

uploaded_file = st.file_uploader("File Upload", type={"pdf"})

if uploaded_file is not None:
    file_name = uploaded_file.name
    file_contents = uploaded_file.read()

    with open("../../llm_application/data/" + file_name, "wb") as f:
        f.write(file_contents)

        with pdfplumber.open("../../llm_application/data/" + file_name) as pdf:
            paragraph = []
            page_no = []
            openai_embedding = []
            for page_num in range(len(pdf.pages)):
                st.write(f"# {page_num}")
                page = pdf.pages[page_num]
                text = page.extract_text()
                st.write(text)

                paragraph.append(text)
                page_no.append(page_num+1)
                openai_embedding.append(get_embedding(text))

            paragraph_dict = {"paragraph": paragraph, "page_no": page_no, "openai_embedding": openai_embedding}
            with open('paragraphs.pickle', 'wb') as f:
                pickle.dump(paragraph_dict, f)

