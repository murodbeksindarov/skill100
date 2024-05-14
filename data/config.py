from environs import Env
# import os
# # environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# # .env fayl ichidan quyidagilarni o'qiymiz


import os
BOT_TOKEN= env.str("BOT_TOKEN")
IP= env.str('ip')
ADMINS=env.list('ADMINS')

kanallar = []
video_kanal = ['@IELTS_CEFR_lesson']
