from aiogram import types
from aiogram.utils.deep_linking import get_start_link
from aiogram.utils.markdown import quote_html, hbold
from loader import dp,db,bot

@dp.message_handler(text='👤 Ma\'lumotlar')
async def balans(message: types.Message):
    balans = db.select_user(message.from_user.id)
    text = f"Sizning ballingiz: {balans[0][4]} \n"
    text += f"Sizning id <code>{message.from_user.id}</code>\n"
    text += f"👥<b>Taklif qilgan do'stlaringiz:</b> <code>{len(db.get_invited(referral=message.from_user.id))}</code> odam\n"
    text += f"📱<b>Hisob raqamingiz:</b> {balans[0][5]}"
    await bot.send_message(message.from_user.id,text=text)

@dp.message_handler(text='📢 Tanlovda ishtirok etish ☑️')
async def Money(message: types.Message):
    user_id = message.from_user.id
    link = await get_start_link(user_id)
    bot_get = await bot.get_me()
    await bot.send_message(user_id, f"<b>🎈 <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> unikal havola-taklifnomasi.</b>\n\n"
                        f"<b>👇 Boshlash uchun bosing:</b>\n"
                        f"{link}")



@dp.inline_handler()
async def referals(inline_query: types.InlineQuery):
    user_id =inline_query.from_user.id
    link = await get_start_link(user_id)
    bot_get = await bot.get_me()
    text = f"{link}"

    input_content = types.InputTextMessageContent(text,disable_web_page_preview=True)
    inl = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("✅ Boshlash ✅", url=f"{link}"))
    referal = types.InlineQueryResultArticle(
        id='01',
        thumb_url=None,
        title="Do'stlarga yuborish 📲",
        description="Do'stlarga yuborish uchun shu yerni bosing",
        input_message_content=input_content,
        reply_markup=inl,
    )
    lis = [referal]
    msg = await inline_query.answer(results=lis, cache_time=1)


# @dp.message_handler(text="📊 Reyting")
# async def delete(message: types.Message):
#     top = db.top()
#     print(top)
#     balans = db.select_user(message.from_user.id)
#     if len(top) > 0:
#         text = f"Top 📊 ta eng yuqori bal to'plaganlar!\n\n"
#         n = 1
#         for i in enumerate(top, start=1):
#             # text += f"{hbold(n)}. {i[2]}, {i[4]} ball\n"
#             # n += 1
#             print(i)
#     # await message.reply(text=f"{text}\n\n"
#     #                          f"Sizning balingiz: {balans[0][4]}")


# @dp.message_handler(text="🎁 Sovg\'alar")
# async def delete(message: types.Message):
#     sovga = db.select_sovga(id=1)
#     await message.reply(
#                 text=f"{sovga[0][1]}")

# @dp.message_handler(text="💡 Shartlar")
# async def shartlar(message: types.Message):
#     await message.answer(text="""Tanlov shartlari juda ham oddiy ✅

# Siz o’zingizning “shaxsiy taklif havolangiz”ni imkon qadar ko’proq do’stlaringiz, yaqinlaringiz va guruhdoshlaringiz bilan ulashing.

# Aynan qancha ko’p inson sizning “taklif havolangiz” orqali botdan ro’yxatdan o’tsa va barcha kanallarga a’zo bo’lsa, sizning sovrinlarni ham yutish ehtimolligingiz shuncha ortadi.

# Sizni g’oliblar qatorida ko’rishdan mamnun bo’lamiz 🔥

# ❗️Tanlov davomida har bir ishtirokchi faqat bitta profildan ishtirok etishi mumkin, ikki yoki undan koʻp profillar orqali ishtirok etish holatlari aniqlansa, oʻsha ishtirokchining natijasi bekor qilinadi va oʻzi tanlovdan chetlashtiriladi ❗️

# Nakrutka urganlar, multi accauntdan qo'shganlar konkursdan chetlashtiriladi. ❌

# Yolg'on reklama bilan ham konkursda qatnashganlar ham chetlatiladi va ballari bekor bo'ladi. 

# Allohdan qo'rqinglar. ❤️""")