import telegram
import os
from dotenv import load_dotenv

load_dotenv()
tk = os.environ['BOT_TOKEN']
bot = telegram.Bot(token=tk)
a = bot.get_me()
print(a)