import requests
import argparse
import os
from create_path_for_images import save_photo_in_folder
from dotenv import load_dotenv


def get_spacex_link(id):
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{id}')
    response.raise_for_status()
    images = response.json()['links']['flickr']['original']
    return images


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='поиск фотографий с API и загрузка их в папку программы. Для spacex нужен id номер конкретного запуска ракеты, иначе будет найден последний запуск.')
    parser.add_argument('--id', help='необходимый id запуска', default='5eb87d46ffd86e000604b388')
    args = parser.parse_args()
    try:
        images = get_spacex_link(args.id)
        for image_number, image_link in enumerate(images):
            file_name = 'spacex'
            save_photo_in_folder(file_name, image_link, image_number)
    except requests.exceptions.HTTPError as error:
        print(error)