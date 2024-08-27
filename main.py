import os, errno
import requests
import argparse
from fetch_spacex_images import spacex_assigned_numbers, get_spacex_link
from apod_images import add_day_images, get_apod_images
from epic_images import get_epic, get_image_epic
from dotenv import load_dotenv
from tg_bot import time_stop


nasa_url = 'https://apod.nasa.gov/apod/image/2402/Ngc1566_HubbleWebb_960.jpg'

if not os.path.exists('images'):
    os.makedirs('images')


def image_format(nasa_url):
    split = os.path.splitext(nasa_url)[1]
    return split


def add_image(nasa_url, filename):
    response = requests.get(nasa_url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description='поиск фотографий с API NASA и выгрузка их в телеграмм с помощью бота, можно настроить время интервала между выкладыванием фото (по умолчанию 4 часа). Для spacex нужен id номер конкретного запуска ракеты, иначе будет найден последний запуск.')
    parser.add_argument('--id', help='необходимый id запуска', default='5eb87d46ffd86e000604b388')
    parser.add_argument('--time', default=14400, help='промежуток времени (в секундах), обозначающий интервал, через который будут отправляться фотографии ботом', type=int)
    args = parser.parse_args()

    try:
        images = get_spacex_link(args.id)
        spacex_assigned_numbers(images)

    except requests.exceptions.HTTPError as error:
        print(error)

    token = os.environ['TOKEN']
    image_format(nasa_url)
    filename = f'images/image_nasa.{image_format(nasa_url)}'
    add_image(nasa_url, filename)
    image_format(nasa_url)
    response_apod = get_apod_images(token)
    add_day_images(response_apod)
    response_epic = get_image_epic(token)
    get_epic(response_epic)

    try:
        time_stop(args.time)


    except requests.exceptions.HTTPError as error:
        print(error)
