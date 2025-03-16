
import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

TG_TOKEN = '7737861074:AAG1h_x5FrmzzhZR7WPX5Wn1jqr1Fq9LvP8'
GEMINI_API_KEY = 'AIzaSyA4vZi85J8ByVHXfINfXub3eRcrmAgAiso'

if not TG_TOKEN or not GEMINI_API_KEY:
    raise ValueError("Ошибка: TG_TOKEN и GEMINI_API_KEY не найдены в .env!")
