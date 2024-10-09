import os
import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from dotenv import load_dotenv
from Handlers import router


load_dotenv(dotenv_path="C:\\Users\\nikit\\PycharmProjects\\habit_tracker_bot\\.evn")

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("токен бота не найден. Проверьте файл .env")


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

#основные функции

async def set_bot_description():
    description_text = ("Я бот для отслеживания привычек. Нажав /start, вы соглашаетесь с обработкой персональных данных. \n \n Для начала нажмите /start.")
    await bot.set_my_description(description_text)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await set_bot_description()
    dp.include_router(router)  #маршрутизатор
    await dp.start_polling(bot)  # запрос к тг

