import os
from dotenv import load_dotenv
from google import genai

from retriever import retrieve_context

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found.")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Ask user for a question
question = input("Ask your medical question: ")

# Retrieve relevant context
context = retrieve_context(question)

# Build the prompt
prompt = f"""
You are a helpful medical assistant.

Answer the user's question ONLY using the information provided below.

Context:
{context}

Question:
{question}

Answer:
"""

# Generate response
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt
)

print("\nAI Response:\n")
print(response.text)