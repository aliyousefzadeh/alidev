import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

@dp.message(F.text == "/start")
async def send_welcome(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="English")],
            [KeyboardButton(text="فارسی")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer("Choose a language:", reply_markup=keyboard)

@dp.message(F.text.in_(["English", "فارسی"]))
async def language_selected(message: types.Message):
    if message.text == "English":
        await message.answer("You selected English")
    elif message.text == "فارسی":
        await message.answer("شما فارسی را انتخاب کردید")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
