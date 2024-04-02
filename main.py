import os, errno
import requests
import argparse
from fetch_spacex_images import fetch_spacex_last_launch
from apod_images import add_day_images
from epic_images import get_epic
from dotenv import load_dotenv
load_dotenv()


token = os.environ['TOKEN']
nasa_url = 'https://apod.nasa.gov/apod/image/2402/Ngc1566_HubbleWebb_960.jpg'

response_one = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
response_one.raise_for_status()
images = response_one.json()['links']['flickr']['original']

response_two = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={token}&count=30')
response_two.raise_for_status()

response_three = requests.get(f'https://api.nasa.gov/EPIC/api/natural?api_key={token}')
response_three.raise_for_status()


if not os.path.exists('images'):
    os.makedirs('images')


def image_format(nasa_url):
    split = os.path.splitext(nasa_url)[1]
    return split

filename = f'images/image_nasa.{image_format(nasa_url)}'

def add_image(nasa_url, filename):
    response = requests.get(nasa_url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


if __name__ == "__main__":
    add_image(nasa_url, filename)
    fetch_spacex_last_launch(images)
    image_format(nasa_url)
    add_day_images(response_two)
    get_epic(response_three, token)