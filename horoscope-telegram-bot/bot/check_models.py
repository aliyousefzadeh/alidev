import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=GEMINI_API_KEY)

print("Listing available models for your API key...")
print("-" * 30)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(f"Model Name: {m.name}")
    print(f"  - Display Name: {m.display_name}")
    print(f"  - Description: {m.description[:100]}...") # Print first 100 chars
    print("-" * 20)