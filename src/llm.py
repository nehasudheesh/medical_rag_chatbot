import os

from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

# Create Gemini client
client = genai.Client(api_key=api_key)

print("Testing Gemini...\n")

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain malaria in 3 simple sentences."
)

print(response.text)