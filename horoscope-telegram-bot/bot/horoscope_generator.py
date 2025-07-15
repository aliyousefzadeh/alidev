# horoscope_generator.py

import os
import logging
import openai
import google.generativeai as genai
from dotenv import load_dotenv
from openai import AsyncOpenAI

# --- Configuration ---
load_dotenv()
PROVIDER = os.getenv("PROVIDER", "openai").lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# --- Initialize AI Clients ---
# This is done once when the module is imported
openai_client = None
gemini_model = None

if PROVIDER == "openai":
    if not OPENAI_API_KEY:
        raise ValueError("PROVIDER is 'openai' but OPENAI_API_KEY is not set.")
    openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)
elif PROVIDER == "gemini":
    if not GEMINI_API_KEY:
        raise ValueError("PROVIDER is 'gemini' but GEMINI_API_KEY is not set.")
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel('gemini-1.5-flash-latest')
else:
    logging.warning(f"Invalid AI_PROVIDER: '{PROVIDER}'. The generator will not work.")

# A mapping from short language codes to full names for a better prompt
LANGUAGE_MAP = {
    "en": "English", "es": "Spanish", "fr": "French", "fa": "Persian"
}

def build_prompt(language_code: str, city: str, birth_date: str) -> str:
    """Constructs the detailed prompt for the AI."""
    language_full_name = LANGUAGE_MAP.get(language_code, "English")
    
    prompt = (
        f"You are a wise and mystical Vedic astrologer, well-versed in Jyotish Shastra, specializing in detailed and insightful readings. "
        f"Generate a personal horoscope for an individual with the following details:\n"
        f"- Date of Birth: {birth_date}\n"
        f"- City of Birth: {city}\n\n"
        f"Your response should be comprehensive and cover:\n"
        f"1.  **Personality Traits:** Based on their sun sign and other astrological factors.\n"
        f"2.  **Life Path and Purpose:** General guidance on their potential direction in life.\n"
        f"3.  **Career Forecast:** Potential strengths, weaknesses, and suitable career paths.\n"
        f"4.  **Love and Relationships:** Insights into their approach to relationships and compatibility.\n"
        f"5.  **Health and Wellness:** Astrological advice for maintaining well-being.\n\n"
        f"The entire response must be written in fluent **{language_full_name}**. "
        f"Format the response with clear headings and paragraphs for readability."
    )
    return prompt

async def generate_horoscope(language: str, city: str, birth_date: str) -> str | None:
    """
    Generates a horoscope using the configured AI provider.
    Returns the horoscope text as a string, or None if an error occurs.
    """
    if PROVIDER not in ["openai", "gemini"]:
        logging.error("AI provider not configured correctly.")
        return None

    prompt = build_prompt(language, city, birth_date)
    
    try:
        logging.info(f"Generating horoscope with {PROVIDER} for user...")
        if PROVIDER == "openai" and openai_client:
            response = await openai_client.chat.completions.create(
                model="gpt-4o",  # Using gpt-4o for better performance/cost
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        
        elif PROVIDER == "gemini" and gemini_model:
            response = await gemini_model.generate_content_async(prompt)
            return response.text
        
    except Exception as e:
        logging.error(f"AI provider error ({PROVIDER}): {e}")
        return None

    return None # Fallback