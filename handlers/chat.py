import google.generativeai as genai
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import GEMINI_API_KEY

router = Router()
user_modes = {}

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-pro-exp")

# keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="💬 Обычный чат"), KeyboardButton(text="🎭 Философ")],
#         [KeyboardButton(text="😂 Юморист"), KeyboardButton(text="🕵️‍♂️ Секретный агент")],
#         [KeyboardButton(text="🔮 Гадалка")]
#     ],
#     resize_keyboard=True
# )

MODE_PROMPTS = {
    "Обычный чат": "Ты дружелюбный бот, который помогает пользователям.",
    "Философ": "Ты философ, который отвечает глубокомысленно.",
    "Юморист": "Ты комик, который отвечает с юмором.",
    "Секретный агент": "Ты секретный агент, который отвечает загадочно.",
    "Гадалка": "Ты мистическая гадалка, которая предсказывает будущее."
}
#
# @router.message(Command("chat"))
# async def start_chat_mode(message: types.Message):
#     user_modes[message.from_user.id] = "Обычный чат"
#     await message.answer("Вы в режиме чата. Выберите стиль общения:", reply_markup=keyboard)

@router.message(lambda msg: msg.text in MODE_PROMPTS)
async def change_mode(message: types.Message):
    user_modes[message.from_user.id] = message.text
    await message.answer(f"Теперь я отвечаю в стиле: {message.text}", parse_mode="Markdown")

@router.message()
async def chat_with_gemini(message: types.Message):
    user_mode = user_modes.get(message.from_user.id, "Обычный чат")
    prompt = MODE_PROMPTS[user_mode]
    response = model.generate_content(f"{prompt}\n\nПользователь: {message.text}")
    bot_response = response.text if response.text else "Ошибка: пустой ответ от AI."
    await message.reply(bot_response)
