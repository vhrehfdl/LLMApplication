import json

from prompts import SUMMARY_PROMPT
from flask import Flask, request
from openai_call import get_chat_openai

app = Flask(__name__)


@app.route("/llm_summary/predict", methods=["GET", "POST"])
def llm_summary():
    params = json.loads(request.get_data(), encoding="utf-8")

    text = params["text"]
    language = params["language"]

    prompt = SUMMARY_PROMPT.format(text=text, language=language)
    result_summary = get_chat_openai(prompt)

    return {"summary": result_summary}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="1000")
