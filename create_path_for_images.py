import os
import requests
import traceback
from dotenv import load_dotenv


if not os.path.exists('images'):
    os.makedirs('images')


def save_photo_in_folder(file_name, image_link, image_number, *args):
    try:
        response = requests.get(image_link, *args)
        response.raise_for_status()
        with open(f'images/{file_name}_{image_number}.jpg', 'wb') as file:
            file.write(response.content)
    except Exception as error:
        print(error)
        