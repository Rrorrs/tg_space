import telegram
import requests
import os
from dotenv import load_dotenv
import random
from PIL import Image
import time
import argparse



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


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='поиск фотографий с API NASA и выгрузка их в телеграмм с помощью бота, можно настроить время интервала между выкладыванием фото (по умолчанию 4 часа). Для spacex нужен id номер конкретного запуска ракеты, иначе будет найден последний запуск.')
    parser.add_argument('--time', default=14400, help='промежуток времени (в секундах), обозначающий интервал, через который будут отправляться фотографии ботом', type=int)
    args = parser.parse_args()
    try:
        time_stop(args.time)


    except requests.exceptions.HTTPError as error:
        print(error)
