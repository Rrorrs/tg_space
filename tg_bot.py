import telegram
import os
from dotenv import load_dotenv
import random
from PIL import Image
import time


def time_stop(stop):
    load_dotenv()
    tk = os.environ['BOT_TOKEN']
    bot = telegram.Bot(token=tk)
    while True:
        folder = os.walk("images")
        for folder_parametrs in folder:
            dirpath, dirnames, filenames = folder_parametrs
        random.shuffle(filenames)
        for photo in filenames:
            image = Image.open(f'images/{photo}')
            bot.send_photo(chat_id='@space_nas', photo=open(f'images/{photo}', 'rb'))
            time.sleep(stop)

