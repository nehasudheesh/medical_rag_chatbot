import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

# Read the API key
api_key = os.getenv("GEMINI_API_KEY")

# Check if API key exists
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file."
    )

# Create Gemini client
client = genai.Client(api_key=api_key)


def generate_answer(context, question):
    """
    Generate an answer using Gemini based on the retrieved context.
    """

    prompt = f"""
You are a helpful medical assistant.

Use ONLY the information given below to answer the user's question.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text


# Test the file independently
if __name__ == "__main__":
    print("Testing Gemini...\n")

    answer = generate_answer(
        "Malaria is a mosquito-borne infectious disease caused by Plasmodium parasites.",
        "Tell me about malaria."
    )

    print(answer)