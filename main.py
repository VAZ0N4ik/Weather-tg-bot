from aiogram.utils import executor
from weather_tg import Weather_tg_bot

if __name__ == '__main__':
    executor.start_polling(Weather_tg_bot.dp)