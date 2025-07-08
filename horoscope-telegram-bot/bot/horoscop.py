import os
import logging
import openai
import google.generativeai as genai
from dotenv import load_dotenv
from persiantools.jdatetime import JalaliDate
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup
from openai import AsyncOpenAI
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes,
    MessageHandler, filters, ConversationHandler
)

# Logging
logging.basicConfig(level=logging.INFO)

# Constants for conversation
LANGUAGE, BIRTHDAY = range(2)

# Set your keys
# TELEGRAM_BOT_TOKEN = "7551425761:AAGfprr4rnAycm0eX0Ws_5uctac8EurCIqE"
# OPENAI_API_KEY = "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"

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PROVIDER = os.getenv("PROVIDER", "openai").lower()

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

if not TELEGRAM_BOT_TOKEN or not OPENAI_API_KEY:
    raise RuntimeError("Missing TELEGRAM_BOT_TOKEN or OPENAI_API_KEY in .env file")


openai.api_key = OPENAI_API_KEY

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = [["English", "فارسی"]]
    await update.message.reply_text(
        "Please select your language / لطفا زبان خود را انتخاب کنید:",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return LANGUAGE

# Handle language
async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = update.message.text.lower()
    context.user_data["language"] = lang
    if "فارسی" in lang:
        await update.message.reply_text("تاریخ تولد خود را به صورت YYYY-MM-DD وارد کنید:")
    else:
        await update.message.reply_text("Please enter your birthdate in format YYYY-MM-DD:")
    return BIRTHDAY

# Handle birthday input
async def set_birthday(update: Update, context: ContextTypes.DEFAULT_TYPE):
    birthday_str = update.message.text.strip()
    language = context.user_data["language"]

    try:
        year, month, day = map(int, birthday_str.split("-"))
    except ValueError:
        if "فارسی" in language:
            await update.message.reply_text("فرمت تاریخ اشتباه است. لطفاً به صورت YYYY-MM-DD وارد کنید.")
        else:
            await update.message.reply_text("Invalid date format. Please use YYYY-MM-DD.")
        return ConversationHandler.END

    # Detect calendar type
    try:
        if year < 1500:
            # Persian calendar
            g_date = JalaliDate(year, month, day).to_gregorian()
        elif year >= 1900:
            # Gregorian calendar
            g_date = datetime(year, month, day).date()
        else:
            if "فارسی" in language:
                await update.message.reply_text("سال وارد شده معتبر نیست.")
            else:
                await update.message.reply_text("Entered year is invalid.")
            return ConversationHandler.END
    except Exception as e:
        if "فارسی" in language:
            await update.message.reply_text("تاریخ نامعتبر است. لطفا دوباره تلاش کنید.")
        else:
            await update.message.reply_text("Invalid date. Please try again.")
        return ConversationHandler.END

    prompt = (
        f"You are a wise and mystical Vedic astrologer, well-versed in Jyotish Shastra. "
        f"Generate a detailed and insightful horoscope reading based on Vedic astrology for a person born on {g_date}. "
        f"Include interpretations of the person's personality traits, life path, possible challenges, and predictions related to career, love, and health. "
        f"The answer should be in {'Persian' if 'فارسی' in language else 'English'}."
)

    # client = AsyncOpenAI(api_key=OPENAI_API_KEY)
    # === Use OpenAI ===
    if PROVIDER == "openai":
        client = AsyncOpenAI(api_key=OPENAI_API_KEY)
        response = await client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        reply_text = response.choices[0].message.content

    # === Use Gemini ===
    elif PROVIDER == "gemini":
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(prompt)
        reply_text = response.text
    
    else:
        reply_text = "Invalid AI provider configuration."
    
    
    await update.message.reply_text(reply_text)
    return ConversationHandler.END


# Cancel
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Cancelled.")
    return ConversationHandler.END

# Main function
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            LANGUAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_language)],
            BIRTHDAY: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_birthday)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    app.add_handler(conv_handler)

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
