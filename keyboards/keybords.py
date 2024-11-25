from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



balance_button = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [KeyboardButton(text='Balance')]
        ]
)

