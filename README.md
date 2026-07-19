# 🏥 Medical RAG Chatbot

An AI-powered Medical Question Answering system built using Retrieval-Augmented Generation (RAG), FAISS Vector Database, Sentence Transformers, Gemini 2.5 Flash, and Streamlit.

---

## 🚀 Features

- Medical Question Answering
- Retrieval-Augmented Generation (RAG)
- FAISS Vector Search
- Gemini 2.5 Flash Integration
- Streamlit Chat Interface
- Medical Knowledge Base
- Session Chat History
- Retrieved Context Viewer
- Clear Chat Option
- Educational Disclaimer

---

## 🛠 Tech Stack

- Python
- Streamlit
- Google Gemini 2.5 Flash
- FAISS
- Sentence Transformers
- Pandas
- python-dotenv

---

## 📂 Project Structure

```
medical-rag-chatbot/
│
├── app.py
├── data/
│   └── medical_knowledge_base.csv
│
├── vectorstore/
│   └── medical_index.faiss
│
├── src/
│   ├── retriever.py
│   ├── llm.py
│   └── rag.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/nehasudheesh/medical_rag_chatbot.git
```

Move into the project

```bash
cd medical_rag_chatbot
```

Create virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

---

## 💬 Example Questions

- Tell me about Malaria
- Explain Asthma
- What causes Dengue?
- Symptoms of Diabetes
- What is Hypertension?

---

## 📸 Application Features

- Interactive chat interface
- AI-generated medical answers
- Retrieved medical context
- Session-based chat history
- Example questions
- Medical disclaimer

---

## ⚠ Disclaimer

This chatbot is intended only for educational purposes and should not be considered professional medical advice. Always consult a qualified healthcare professional.

---

## 👩‍💻 Author

Neha Sudheesh