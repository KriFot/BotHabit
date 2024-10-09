from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


greet = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Ваши привычки",callback_data='Catalog')],
    [InlineKeyboardButton(text="создать", callback_data="new"),
     InlineKeyboardButton(text="редактировать", callback_data="redact")]
 ])


teft=['1','2','3', '4']
kall=['SartTimer',"new","redact"]
async def catteft():
    keyboard = InlineKeyboardBuilder()
    for n, callback in zip(teft, kall):  # Объединяем значения и колбэки
        keyboard.add(InlineKeyboardButton(text=n, callback_data=callback))  # Используем callback_data
    return keyboard.adjust(2).as_markup()