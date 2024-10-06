from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


greet = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Ваши привычки",callback_data='Catalog')],
    [InlineKeyboardButton(text="создать", callback_data="new"),
     InlineKeyboardButton(text="редактировать", callback_data="redact")]
 ])


teft=['1','2','3']
async def catteft():
    keyboard = InlineKeyboardBuilder()
    for n in teft:
        keyboard.add(InlineKeyboardButton(text=n, url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
    return keyboard.adjust(2).as_markup()