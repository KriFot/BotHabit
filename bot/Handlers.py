from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def send_welcome(message: Message):
    await message.answer("привет! \n \n Мои команды: \n /help")


@router.message(Command("help"))
async def send_welcome(message: Message):
    await message.answer("прости, я пока ничего не умею(")
