FROM python:3.8.10
WORKDIR /llm_application

RUN pip install --upgrade pip

RUN pip install openai
RUN pip install streamlit
RUN pip install flask
RUN pip install scikit-learn
RUN pip install pdfplumber


COPY . .
#CMD ["streamlit", "run", "app_gpt_demo.py"]
CMD tail -f /dev/null