from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

router = Router()
user_expressions = {}


@router.message(F.text)
async def calculate(message: types.Message):
    chat_id = message.chat.id
    text = message.text

    if text == "C":
        user_expressions[chat_id] = ""
        await message.answer("Очищено!")
    elif text == "=":
        try:
            result = eval(user_expressions.get(chat_id, "0"))
            await message.answer(f"Результат: {result}")
            user_expressions[chat_id] = str(result)
        except:
            await message.answer("Ошибка в выражении!")
            user_expressions[chat_id] = ""
    else:
        user_expressions[chat_id] = user_expressions.get(chat_id, "") + text
        await message.answer(user_expressions[chat_id])
