SUMMARY_PROMPT = f"""{{text}}
---
Must respond in {{language}}.
Tl;dr
"""

TRANSLATE_PROMPT = f"""sentence={{text}}
---
sentence를 번역해주세요.
Must respond in {{language}}.
"""


SEARCH_PROMPT = f"""context={{context}} \n
question={{question}} \n

context를 기반으로 question에 대한 답변을 생성해주세요.
"""
