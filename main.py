import os
import requests
from dotenv import load_dotenv


nasa_url = 'https://apod.nasa.gov/apod/image/2402/Ngc1566_HubbleWebb_960.jpg'

if not os.path.exists('images'):
    os.makedirs('images')


def separates_image_format(nasa_url):
    split = os.path.splitext(nasa_url)[1]
    return split


def add_image(nasa_url, filename):
    response = requests.get(nasa_url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)

def create_path(file_name, image, image_number):
        response = requests.get(image)
        response.raise_for_status()
        with open(f'images/{file_name}_{image_number}.jpg', 'wb') as file:
            file.write(response.content)


if __name__ == "__main__":
    load_dotenv()
    separates_image_format(nasa_url)
    filename = f'images/image_nasa.{separates_image_format(nasa_url)}'
    add_image(nasa_url, filename)
    separates_image_format(nasa_url)
