
def query(user_query):
    from google import genai
    api_key="AIzaSyAwCE3eqv-MA4ZkoPnFkuAyc8O-ZZfyMVo"
    my_ai= genai.Client(api_key=api_key)
    response=my_ai.models.generate_content(
        model="gemini-3-flash-preview",
        contents=user_query)

    return response.text

import streamlit as st

st.title("Personal AI Chatbot")

user_input = st.chat_input("enter your Query")
if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            result = query(user_input)
            st.markdown(result)