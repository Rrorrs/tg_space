import telegram
import requests
import os
from dotenv import load_dotenv
import random
import time
import argparse



def uploading_photos_by_bot(stop, id_address):
    load_dotenv()
    tg_token = os.environ['TG_BOT_TOKEN']
    bot = telegram.Bot(token=tg_token)
    while True:
        folder = os.walk("images")
        for folder_parametrs in folder:
            dirpath, dirnames, filenames = folder_parametrs
        random.shuffle(filenames)
        for photo in filenames:
            bot.send_photo(chat_id=f'@{id_address}', photo=open(f'images/{photo}', 'rb'))
            time.sleep(stop)


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Выгрузка фотографий в телеграмм с помощью бота, можно настроить время интервала между выкладыванием фото (по умолчанию 4 часа). ')
    parser.add_argument('--time', default=14400, help='промежуток времени (в секундах), обозначающий интервал, через который будут отправляться фотографии ботом', type=int)
    parser.add_argument('--tg_id', help='ваш адрес телеграмма, на который будут отправляться фото')
    args = parser.parse_args()
    try:
        uploading_photos_by_bot(stop=args.time, id_address=args.tg_id)
    except requests.exceptions.HTTPError as error:
        print('Введен неверный тип данных, время должно записываться только числами')

    