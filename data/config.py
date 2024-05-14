from environs import Env
import os
# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# # .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")
IP = env.str('ip')
ADMINS = env.list('ADMINS')
#
# import os
# BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
# IP = str(os.environ.get("ip"))
# ADMINS = list(os.environ.get('ADMINS'))


kanallar = []
video_kanal = ['@IELTS_CEFR_lesson']
