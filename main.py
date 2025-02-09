import executor
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, types
# from config import TOKEN_API

# Загружаем переменные из .env файла
load_dotenv()

# Получаем токен бота
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_upper(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)

