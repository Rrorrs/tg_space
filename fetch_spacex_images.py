import requests
import argparse
import os
from path_for_images import create_path
from dotenv import load_dotenv
load_dotenv()


token = os.environ['NASA_TOKEN']


def get_spacex_link(id):
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{id}')
    response.raise_for_status()
    images = response.json()['links']['flickr']['original']
    return images


def spacex_index_generation(images):
    for image_number, image in enumerate(images):
        file_name = 'spacex'
        create_path(file_name, image, image_number)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='поиск фотографий с API NASA и выгрузка их в телеграмм с помощью бота, можно настроить время интервала между выкладыванием фото (по умолчанию 4 часа). Для spacex нужен id номер конкретного запуска ракеты, иначе будет найден последний запуск.')
    parser.add_argument('--id', help='необходимый id запуска', default='5eb87d46ffd86e000604b388')
    args = parser.parse_args()
    try:
        images = get_spacex_link(args.id)
        spacex_index_generation(images)
    except requests.exceptions.HTTPError as error:
        print("Неверно введён id запуска")