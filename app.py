import time
import streamlit as st
from src.rag import ask_rag
from src.retriever import retrieve_context

st.set_page_config(
    page_title="Medical RAG Chatbot",
    page_icon="🏥",
    layout="wide"
)

# ==========================
# Sidebar
# ==========================
with st.sidebar:

    st.title("🏥 Medical RAG Chatbot")
    st.write("AI-powered Medical Question Answering")

    st.markdown("---")

    st.info(
        "This chatbot answers questions using a medical knowledge base and Gemini AI."
    )

    st.markdown("---")

    st.subheader("🤖 AI Model")
    st.write("**LLM:** Gemini 2.5 Flash")
    st.write("**Embeddings:** all-MiniLM-L6-v2")
    st.write("**Vector Store:** FAISS")

    st.markdown("---")

    st.subheader("📊 Knowledge Base")
    st.metric("Diseases", "38")
    st.metric("Embedding Model", "MiniLM")
    st.metric("Vector Store", "FAISS")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ==========================
# Main Page
# ==========================

st.title("🏥 Medical RAG Chatbot")
st.write("Ask medical questions based on the knowledge base.")

st.warning(
    "⚠ This chatbot is for educational purposes only. "
    "Always consult a qualified healthcare professional for medical advice."
)

# ==========================
# Session State
# ==========================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================
# Welcome Screen
# ==========================

if len(st.session_state.messages) == 0:

    st.info(
        """
### 💡 Example Questions

- Tell me about Malaria
- Explain Asthma
- What causes Dengue?
- Symptoms of Diabetes
- What is Hypertension?
"""
    )

# ==========================
# Display Chat History
# ==========================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================
# Chat Input
# ==========================

question = st.chat_input("Ask a medical question...")

if question:

    question = question.strip()

    if question == "":
        st.warning("Please enter a medical question.")
        st.stop()

    # User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Generate Answer
    start = time.time()

    with st.spinner("🔍 Searching medical knowledge and generating answer..."):

        context = retrieve_context(question)

        answer = ask_rag(question)

    end = time.time()

    # Assistant Message
    with st.chat_message("assistant"):

        st.success("Answer generated successfully!")

        st.markdown(answer)

        st.caption(f"⏱ Response generated in {end-start:.2f} seconds")

        with st.expander("📚 View Retrieved Medical Knowledge"):

            st.write(context)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# ==========================
# Footer
# ==========================

st.markdown("---")

st.caption(
    "🏥 Medical RAG Chatbot | Built using Streamlit + Gemini AI + FAISS + Sentence Transformers"
)