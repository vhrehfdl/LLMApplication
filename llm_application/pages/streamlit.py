import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# 텍스트 입력 받기
user_input = st.text_input("이름을 입력하세요:", "홍길동")

# 숫자 입력 받기
age = st.number_input("나이를 입력하세요:", min_value=0, max_value=150, value=25)

# 버튼 클릭 여부 확인
if st.button("확인"):
    # 입력된 정보 출력
    st.write(f"이름: {user_input}")
    st.write(f"나이: {age}")
