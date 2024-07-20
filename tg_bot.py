import telegram
import os
from dotenv import load_dotenv

load_dotenv()
tk = os.environ['BOT_TOKEN']
bot = telegram.Bot(token=tk)
a = bot.get_me()

bot.send_photo(chat_id='@space_nas', photo=open('images/nasa_apod_0.jpg', 'rb'))