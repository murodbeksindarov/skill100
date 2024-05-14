from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📢 Tanlovda ishtirok etish ☑️'),
        ],
        [
            KeyboardButton(text='👤 Ma\'lumotlar')
        ],
        [
            KeyboardButton(text='🎁Premium Files')
        ]
    ],resize_keyboard=True
)

darsliklar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='IELTS'),
            KeyboardButton(text='MULTILEVEL')
        ],
        [
            KeyboardButton(text='⬅️ Ortga')
        ]
    ],resize_keyboard=True
)


numbers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Raqamni yuborish 📞',request_contact=True)
        ]
    ],resize_keyboard=True
)
