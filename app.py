import streamlit as st
from src.rag import ask_rag

st.set_page_config(
    page_title="Medical RAG Chatbot",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Medical RAG Chatbot")
st.write("Ask any medical question based on the knowledge base.")

question = st.text_input("Enter your medical question:")

if st.button("Ask"):
    if question:
        answer = ask_rag(question)

        st.subheader("Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question.")