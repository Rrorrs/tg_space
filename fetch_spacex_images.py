import requests
import os
from dotenv import load_dotenv
load_dotenv()


token = os.environ['NASA_TOKEN']


def get_spacex_link(id):
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{id}')
    response.raise_for_status()
    images = response.json()['links']['flickr']['original']
    return images


def spacex_assigned_numbers(images):
    for image_number, image in enumerate(images):
        response = requests.get(image)
        response.raise_for_status()
        with open(f'images/spacex_{image_number}.jpg', 'wb') as file:
            file.write(response.content)

            