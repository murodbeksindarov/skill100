from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

IELTS = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="IELTS", url="https://t.me/IELTS_theme"),
            InlineKeyboardButton(text="FULL MOCK", url="https://t.me/IELTS_CEFR_fullmock")
        ]
    ]
)

def premium_contents():
    prcon = InlineKeyboardMarkup(row_width=1)

    prcon.insert(InlineKeyboardButton(text="Expected Passages 2024⚡", callback_data='Buy Something'))
    prcon.insert(InlineKeyboardButton(text=" 5 STARS ⚡", callback_data='Buy Something2'))


    return prcon

MULTILEVEL = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="MULTILEVEL", url="https://t.me/MULTILEVEL_theme"),
            InlineKeyboardButton(text="FULL MOCK", url="https://t.me/IELTS_CEFR_fullmock")
        ]
    ]
)


