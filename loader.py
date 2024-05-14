from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.sqlite3 import Database
from data import config
from keyboards import inline

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database(path_to_db='data.db')

@dp.message_handler(text="🎁Premium Files")
async def bot_message(message: types.Message):
    await bot.send_message(message.from_user.id,f"We want to provide you the PREMIUM PACKETS 🎯\n\nEach of the choices below worth 15 points‼", reply_markup=inline.premium_contents())


    
@dp.callback_query_handler(text="Buy Something")
async def balance_handler(message: types.Message):
    user_id = message.from_user.id
    amount_spent = 15
    await bot.delete_message(message.from_user.id, message.message.message_id)
    user_balance = db.select_user(message.from_user.id)[0][4]

    
    
    if user_balance is None:
        user_balance = 0
    if int(user_balance) >= amount_spent:
            db.deduct_balance(user_id, amount_spent)
            # Inform the user about the successful purchase
            await bot.send_message(message.from_user.id, f"Your Purchase was successful‼✅\n\nYour updated balance: "
                                                            f"{int(user_balance) - amount_spent} points")
            chat_id = -1002139663305
            invite_link = await bot.create_chat_invite_link(chat_id=chat_id, member_limit=1)
            await bot.send_message(message.from_user.id, f"Here is your invite link: {invite_link.invite_link}")
            
            await bot.send_message(message.from_user.id, "Rahmat !")
            
        
    else:
        await bot.send_message(message.from_user.id, f"You don't have enough points. You need to gain {amount_spent - int(user_balance)} more points !")



@dp.callback_query_handler(text="Buy Something2")
async def balance_handler(message: types.Message):
    user_id = message.from_user.id
    amount_spent = 15
    await bot.delete_message(message.from_user.id, message.message.message_id)
    user_balance = db.select_user(message.from_user.id)[0][4]

    
    
    if user_balance is None:
        user_balance = 0
    if int(user_balance) >= amount_spent:
            db.deduct_balance(user_id, amount_spent)
            # Inform the user about the successful purchase
            await bot.send_message(message.from_user.id, f"Your Purchase was successful‼✅\n\nYour updated balance: "
                                                            f"{int(user_balance) - amount_spent} points")
            chat_id = -1002135414566
            invite_link = await bot.create_chat_invite_link(chat_id=chat_id, member_limit=1)
            await bot.send_message(message.from_user.id, f"Here is your invite link: {invite_link.invite_link}")
            
            await bot.send_message(message.from_user.id, "Rahmat !")
            
        
    else:
        await bot.send_message(message.from_user.id, f"You don't have enough points. You need to gain {amount_spent - int(user_balance)} more points !")
