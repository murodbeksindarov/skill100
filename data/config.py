from environs import Env
<<<<<<< HEAD
# import os
# # environs kutubxonasidan foydalanish
=======
import os
# environs kutubxonasidan foydalanish
>>>>>>> 0e50f7c71c6446b4a48c29cf2e1640db4d9c169c
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


<<<<<<< HEAD
import os
BOT_TOKEN= env.str("BOT_TOKEN")
IP= env.str('ip')
ADMINS=env.list('ADMINS')

=======
>>>>>>> 0e50f7c71c6446b4a48c29cf2e1640db4d9c169c
kanallar = []
video_kanal = ['@IELTS_CEFR_lesson']
