import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Configure logging
logging.basicConfig(level=logging.INFO)

# Bot token - replace with your actual bot token
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Define states for the conversation
class UserRegistration(StatesGroup):
    waiting_for_language = State()
    waiting_for_city = State()
    waiting_for_birth_date = State()

# Available languages
LANGUAGES = {
    "en": "🇺🇸 English",
    "es": "🇪🇸 Español", 
    "fr": "🇫🇷 Français",
    "de": "🇩🇪 Deutsch",
    "it": "🇮🇹 Italiano",
    "pt": "🇧🇷 Português",
    "ru": "🇷🇺 Русский",
    "zh": "🇨🇳 中文",
    "ja": "🇯🇵 日本語",
    "ko": "🇰🇷 한국어"
}

# Language-specific messages
MESSAGES = {
    "en": {
        "welcome": "👋 Welcome! Please select your preferred language:",
        "language_selected": "✅ Language set to English. Now, please enter your city of birth:",
        "enter_city": "🏙️ Please enter your city of birth:",
        "city_received": "✅ City received: {}. Now, please enter your date of birth (YYYY-MM-DD):",
        "enter_birth_date": "📅 Please enter your date of birth in format YYYY-MM-DD:",
        "invalid_date": "❌ Invalid date format. Please use YYYY-MM-DD format:",
        "registration_complete": "🎉 Registration complete!\n\n📋 Your information:\n🌍 Language: English\n🏙️ City of birth: {}\n📅 Date of birth: {}",
        "invalid_date_value": "❌ Invalid date. Please enter a valid date in YYYY-MM-DD format:"
    },
    "es": {
        "welcome": "👋 ¡Bienvenido! Por favor, selecciona tu idioma preferido:",
        "language_selected": "✅ Idioma establecido en Español. Ahora, por favor ingresa tu ciudad de nacimiento:",
        "enter_city": "🏙️ Por favor ingresa tu ciudad de nacimiento:",
        "city_received": "✅ Ciudad recibida: {}. Ahora, por favor ingresa tu fecha de nacimiento (YYYY-MM-DD):",
        "enter_birth_date": "📅 Por favor ingresa tu fecha de nacimiento en formato YYYY-MM-DD:",
        "invalid_date": "❌ Formato de fecha inválido. Por favor usa el formato YYYY-MM-DD:",
        "registration_complete": "🎉 ¡Registro completo!\n\n📋 Tu información:\n🌍 Idioma: Español\n🏙️ Ciudad de nacimiento: {}\n📅 Fecha de nacimiento: {}",
        "invalid_date_value": "❌ Fecha inválida. Por favor ingresa una fecha válida en formato YYYY-MM-DD:"
    },
    "fr": {
        "welcome": "👋 Bienvenue ! Veuillez sélectionner votre langue préférée :",
        "language_selected": "✅ Langue définie en Français. Maintenant, veuillez entrer votre ville de naissance :",
        "enter_city": "🏙️ Veuillez entrer votre ville de naissance :",
        "city_received": "✅ Ville reçue : {}. Maintenant, veuillez entrer votre date de naissance (YYYY-MM-DD) :",
        "enter_birth_date": "📅 Veuillez entrer votre date de naissance au format YYYY-MM-DD :",
        "invalid_date": "❌ Format de date invalide. Veuillez utiliser le format YYYY-MM-DD :",
        "registration_complete": "🎉 Inscription terminée !\n\n📋 Vos informations :\n🌍 Langue : Français\n🏙️ Ville de naissance : {}\n📅 Date de naissance : {}",
        "invalid_date_value": "❌ Date invalide. Veuillez entrer une date valide au format YYYY-MM-DD :"
    }
}

def get_message(lang_code: str, message_key: str) -> str:
    """Get message in specified language, fallback to English if not found"""
    return MESSAGES.get(lang_code, MESSAGES["en"]).get(message_key, MESSAGES["en"][message_key])

def create_language_keyboard() -> InlineKeyboardMarkup:
    """Create inline keyboard with language options"""
    builder = InlineKeyboardBuilder()
    
    # Add language buttons in rows of 2
    for i in range(0, len(LANGUAGES), 2):
        lang_codes = list(LANGUAGES.keys())[i:i+2]
        row_buttons = []
        for code in lang_codes:
            row_buttons.append(InlineKeyboardButton(
                text=LANGUAGES[code],
                callback_data=f"lang_{code}"
            ))
        builder.row(*row_buttons)
    
    return builder.as_markup()

@dp.message(CommandStart())
async def start_command(message: types.Message, state: FSMContext):
    """Handle /start command"""
    keyboard = create_language_keyboard()
    await message.answer(
        "👋 Welcome! Please select your preferred language:",
        reply_markup=keyboard
    )
    await state.set_state(UserRegistration.waiting_for_language)

@dp.callback_query(F.data.startswith("lang_"))
async def language_selected(callback: types.CallbackQuery, state: FSMContext):
    """Handle language selection"""
    lang_code = callback.data.split("_")[1]
    
    # Save selected language to state
    await state.update_data(language=lang_code)
    
    # Get localized message
    message_text = get_message(lang_code, "language_selected")
    
    await callback.message.edit_text(message_text)
    await callback.answer()
    
    # Move to next state
    await state.set_state(UserRegistration.waiting_for_city)

@dp.message(UserRegistration.waiting_for_city)
async def city_received(message: types.Message, state: FSMContext):
    """Handle city of birth input"""
    city = message.text.strip()
    
    # Get user's language
    data = await state.get_data()
    lang_code = data.get("language", "en")
    
    # Save city to state
    await state.update_data(city=city)
    
    # Get localized message
    message_text = get_message(lang_code, "city_received").format(city)
    
    await message.answer(message_text)
    
    # Move to next state
    await state.set_state(UserRegistration.waiting_for_birth_date)

@dp.message(UserRegistration.waiting_for_birth_date)
async def birth_date_received(message: types.Message, state: FSMContext):
    """Handle birth date input"""
    date_text = message.text.strip()
    
    # Get user's language
    data = await state.get_data()
    lang_code = data.get("language", "en")
    
    try:
        # Validate date format
        birth_date = datetime.strptime(date_text, "%Y-%m-%d")
        
        # Check if date is not in the future
        if birth_date > datetime.now():
            await message.answer(get_message(lang_code, "invalid_date_value"))
            return
        
        # Save birth date to state
        await state.update_data(birth_date=date_text)
        
        # Get all collected data
        data = await state.get_data()
        city = data.get("city")
        language_name = LANGUAGES.get(lang_code, "English")
        
        # Send completion message
        completion_message = get_message(lang_code, "registration_complete").format(city, date_text)
        await message.answer(completion_message)
        
        # Clear state
        await state.clear()
        
        # Log the registration (in production, save to database)
        logging.info(f"User {message.from_user.id} registered: Language={lang_code}, City={city}, Birth Date={date_text}")
        
    except ValueError:
        # Invalid date format
        await message.answer(get_message(lang_code, "invalid_date"))

@dp.message()
async def handle_unexpected_message(message: types.Message, state: FSMContext):
    """Handle unexpected messages during registration flow"""
    current_state = await state.get_state()
    data = await state.get_data()
    lang_code = data.get("language", "en")
    
    if current_state == UserRegistration.waiting_for_language:
        # User sent text instead of selecting language
        keyboard = create_language_keyboard()
        await message.answer(
            get_message(lang_code, "welcome"),
            reply_markup=keyboard
        )
    elif current_state == UserRegistration.waiting_for_city:
        await message.answer(get_message(lang_code, "enter_city"))
    elif current_state == UserRegistration.waiting_for_birth_date:
        await message.answer(get_message(lang_code, "enter_birth_date"))

async def main():
    """Main function to start the bot"""
    try:
        logging.info("Starting bot...")
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Error: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())