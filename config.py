
import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

TG_TOKEN = os.getenv("TG_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not TG_TOKEN or not GEMINI_API_KEY:
    raise ValueError("Ошибка: TG_TOKEN и GEMINI_API_KEY не найдены в .env!")
