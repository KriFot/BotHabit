from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

import bot.KBoards as kb

router = Router()


@router.message(CommandStart())
async def send_welcome(message: Message):
    await message.answer("привет! \n \n Мои команды:", reply_markup=kb.greet)


@router.message(Command("help"))
async def send_welcome(message: Message):
    await message.answer("прости, я пока ничего не умею(")


@router.callback_query(F.data == "Catalog")
async def Catal(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Catalog', reply_markup=await kb.catteft())


@router.callback_query(F.data == "new")
async def new(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('new')


@router.callback_query(F.data == "redact")
async def redact(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('redact')

