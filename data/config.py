from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "Bot tokeni"  # Bot toekn
ADMINS = [Adminning telegram id] # adminlar ro'yxati
