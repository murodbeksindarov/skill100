from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")
#
# import os
# BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
# IP = str(os.environ.get("ip"))
# ADMINS = list(os.environ.get('ADMINS'))


kanallar = []
video_kanal = ['@IELTS_CEFR_lesson']
