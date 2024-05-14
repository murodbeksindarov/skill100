from typing import Union
from aiogram import Bot


# async def chek(user_id, kanal: Union[str, int]):
#     bot = Bot.get_current()
#     azo = await bot.get_chat_member(user_id=user_id, chat_id=kanal)
#     return azo.is_chat_member()

async def chek(user_id, kanal):
    bot = Bot.get_current()
    chat_member = await bot.get_chat_member(user_id=user_id, chat_id=kanal)
    
    # Check if the user's status is 'member'
    if chat_member['status'] == 'left':
        return False
    else:
        return True
