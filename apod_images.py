import requests
import os
from dotenv import load_dotenv
load_dotenv()


def get_apod_images(token):
    payload = {'api_key': f'{token}', 'count': 30}
    response = requests.get(f'https://api.nasa.gov/planetary/apod', params=payload)
    response.raise_for_status()
    return response


def add_day_images(response_apod):
    for block in response_apod.json():
        day_images = block['url']
        if os.path.splitext(day_images)[1] in ['.jpg', '.png']:
            days.append(day_images)

    for image_number, image in enumerate(days):
        response = requests.get(image)
        response.raise_for_status()
        with open(f'images/nasa_apod_{image_number}.jpg', 'wb') as file:
            file.write(response.content)

if __name__=='__main__':

    token = os.environ['NASA_TOKEN']
    days = []
    response_apod = get_apod_images(token)
    add_day_images(response_apod)
