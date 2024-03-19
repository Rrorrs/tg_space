import os, errno
import requests
import datetime
from dotenv import load_dotenv
load_dotenv()


days = []
epic_images = []
TOKEN = os.environ['TOKEN']
nasa_url = 'https://apod.nasa.gov/apod/image/2402/Ngc1566_HubbleWebb_960.jpg'

response_one = requests.get('https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a')
response_one.raise_for_status()
images = response_one.json()['links']['flickr']['original']

response_two = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={TOKEN}&count=30')
response_two.raise_for_status()

response_three = requests.get(f'https://api.nasa.gov/EPIC/api/natural?api_key={TOKEN}')
response_three.raise_for_status()




if not os.path.exists('images'):
    os.makedirs('images')


def image_format(nasa_url):
    split = os.path.splitext(nasa_url)[1]
    return split

filename = f'images/image_nasa.{image_format(nasa_url)}'


def add_day_images(response_two):
    for block in response_two.json():
        day_images = block['url']
        days.append(day_images)

    for image_number, image in enumerate(days):
        response = requests.get(image)
        response.raise_for_status()
        with open(f'images/nasa_apod_{image_number}.jpg', 'wb') as file:
            file.write(response.content)
    

def get_epic(response_three):
    for block in response_three.json():
        name_image = block['image']
        date_image = block['date']
        date_=datetime.datetime.strptime(date_image, '%Y-%m-%d %H:%S:%M')
        date = datetime.datetime.date(date_)
        date = str(date)
        change_date = date.replace('-', '/')
        epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{change_date}/png/{name_image}.png?api_key={TOKEN}'
        epic_images.append(epic_url)

    for image_number, image in enumerate(epic_images):
        response = requests.get(image)
        response.raise_for_status()
        with open(f'images/nasa_epic_{image_number}.png', 'wb') as file:
            file.write(response.content)

  


def fetch_spacex_last_launch(images):
    for image_number, image in enumerate(images):
        response = requests.get(image)
        response.raise_for_status()
        with open(f'images/spacex_{image_number}.jpg', 'wb') as file:
            file.write(response.content)


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
    get_epic(response_three)