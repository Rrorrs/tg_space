import requests
import os
import argparse
import traceback
from dotenv import load_dotenv
from create_path_for_images import save_photo_in_folder



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

    for image_number, image_link in enumerate(apod_photos):
        file_name = 'nasa_apod'
        save_photo_in_folder(file_name, image_link, image_number)


if __name__=='__main__':
    load_dotenv()
    parser = argparse.ArgumentParser(description='поиск фотографий с API и загрузка их в папку программы, для последующего использования ботом.')
    parser.add_argument('--count_load', help='количество фотографий, которое нужно выгрузить', default=30)
    args = parser.parse_args()
    try:
        token = os.environ['NASA_TOKEN']
        response_apod = get_apod_images(token, args.count_load)
        download_day_images(response_apod)
    
    except requests.exceptions.HTTPError as error:
        print(error)