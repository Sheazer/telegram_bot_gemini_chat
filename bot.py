from aiogram import Bot, Dispatcher
from aiogram.filters import StateFilter

from config import TG_TOKEN
from handlers import chat, calculator
from handlers.main import mode_router, ModeStates

bot = Bot(token=TG_TOKEN)
dp = Dispatcher()

dp.include_router(mode_router)
dp.message.register(
    calculator.router.message,
    StateFilter(ModeStates.calculator_mode)
)
dp.message.register(
    chat.router.message,
    StateFilter(ModeStates.chat_mode)
)
