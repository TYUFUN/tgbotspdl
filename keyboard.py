from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Русккий", callback_data="ru"),
        InlineKeyboardButton(text="English", callback_data="en"),
    ]
])
tg = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Telegram channel", url="https://t.me/TYUFUNTG")
    ]
])