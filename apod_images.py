import requests
import os
import argparse
from dotenv import load_dotenv
from create_path_for_images import create_a_folder_with_photo



def get_apod_images(token, count_load):
    payload = {'api_key': f'{token}', 'count': count_load}
    response = requests.get(f'https://api.nasa.gov/planetary/apod', params=payload)
    response.raise_for_status()
    return response


def download_day_images(response_apod):
    apod_photos = []
    for url_on_photo in response_apod.json():
        day_images = url_on_photo['url']
        if os.path.splitext(day_images)[1] in ['.jpg', '.png']:
            apod_photos.append(day_images)

    for image_number, image in enumerate(apod_photos):
        file_name = 'nasa_apod'
        create_a_folder_with_photo(file_name, image, image_number)


if __name__=='__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(description='поиск фотографий с API NASA и выгрузка их в телеграмм с помощью бота, можно настроить время интервала между выкладыванием фото (по умолчанию 4 часа). Для spacex нужен id номер конкретного запуска ракеты, иначе будет найден последний запуск.')
    parser.add_argument('--count_load', help='количество фотографий, которое нужно выгрузить', default=30)
    args = parser.parse_args()
    try:
        token = os.environ['NASA_TOKEN']
        response_apod = get_apod_images(token, args.count_load)
        download_day_images(response_apod)
    
    except requests.exceptions.HTTPError as error:
        print("Неверно введено количество фотографий, это должно быть только число, без пробелов и иных знаков")