import telegram
import requests
import os
from dotenv import load_dotenv
import random
import time
import argparse



def launching_the_bot(stop):
    load_dotenv()
    tg_token = os.environ['TG_BOT_TOKEN']
    bot = telegram.Bot(token=tg_token)
    while True:
        folder = os.walk("images")
        for folder_parametrs in folder:
            dirpath, dirnames, filenames = folder_parametrs
        random.shuffle(filenames)
        for photo in filenames:
            bot.send_photo(chat_id='@space_nas', photo=open(f'images/{photo}', 'rb'))
            time.sleep(stop)


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Выгрузка фотографий в телеграмм с помощью бота, можно настроить время интервала между выкладыванием фото (по умолчанию 4 часа). ')
    parser.add_argument('--time', default=14400, help='промежуток времени (в секундах), обозначающий интервал, через который будут отправляться фотографии ботом', type=int)
    args = parser.parse_args()
    try:
        launching_the_bot(args.time)


    except requests.exceptions.HTTPError as error:
        print('Введен неверный тип данных, время должно записываться только числами')
