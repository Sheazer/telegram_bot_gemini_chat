from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class ModeStates(StatesGroup):
    calculator_mode = State()  # Режим калькулятора
    chat_mode = State()  # Режим чата


mode_router = Router()  # Роутер для управления режимами

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="7"), KeyboardButton(text="8"), KeyboardButton(text="9"), KeyboardButton(text="/")],
        [KeyboardButton(text="4"), KeyboardButton(text="5"), KeyboardButton(text="6"), KeyboardButton(text="*")],
        [KeyboardButton(text="1"), KeyboardButton(text="2"), KeyboardButton(text="3"), KeyboardButton(text="-")],
        [KeyboardButton(text="0"), KeyboardButton(text="."), KeyboardButton(text="="), KeyboardButton(text="+")],
        [KeyboardButton(text="C")]
    ],
    resize_keyboard=True
)


# Обработчик команды /calculator для перехода в режим калькулятора
@mode_router.message(Command("calс"))
async def set_calculator_mode(message: Message, state: FSMContext):
    await state.set_state(ModeStates.calculator_mode)  # Устанавливаем состояние калькулятора
    await message.answer("Вы в режиме калькулятора:", reply_markup=keyboard)


keyboard2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💬 Обычный чат"), KeyboardButton(text="🎭 Философ")],
        [KeyboardButton(text="😂 Юморист"), KeyboardButton(text="🕵️‍♂️ Секретный агент")],
        [KeyboardButton(text="🔮 Гадалка")]
    ],
    resize_keyboard=True
)


# Обработчик команды /chat для перехода в режим чата
@mode_router.message(Command("chat"))
async def set_chat_mode(message: Message, state: FSMContext):
    await state.set_state(ModeStates.chat_mode)  # Устанавливаем состояние чата
    await message.answer("Вы в режиме чата. Выберите стиль общения:", reply_markup=keyboard2)
