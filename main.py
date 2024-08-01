import os, errno
import requests
import argparse
from fetch_spacex_images import fetch_spacex_last_launch, get_spacex_images
from apod_images import add_day_images, get_apod_images
from epic_images import get_epic, get_image_epic
from dotenv import load_dotenv
from tg_bot import time_stop


nasa_url = 'https://apod.nasa.gov/apod/image/2402/Ngc1566_HubbleWebb_960.jpg'

if not os.path.exists('images'):
    os.makedirs('images')


def image_format(nasa_url):
    split = os.path.splitext(nasa_url)[1]
    return split


def add_image(nasa_url, filename):
    response = requests.get(nasa_url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


if __name__ == "__main__":
    load_dotenv()
    parser_spacex = argparse.ArgumentParser()
    parser_spacex.add_argument('--id', help='необходимый id запуска')
    args_spacex = parser_spacex.parse_args()
    try:
        print(args_spacex.id)
        if args_spacex.id:
            images = get_spacex_images(args_spacex.id)
            fetch_spacex_last_launch(images)
        else:
            images = get_spacex_images(id='latest')
            print(images)
            fetch_spacex_last_launch(images)

    except requests.exceptions.HTTPError as error:
        print(error)

    # token = os.environ['TOKEN']
    # image_format(nasa_url)
    # filename = f'images/image_nasa.{image_format(nasa_url)}'
    # add_image(nasa_url, filename)
    # image_format(nasa_url)
    # response_apod = get_apod_images(token)
    # add_day_images(response_apod)
    # response_epic = get_image_epic(token)
    # get_epic(response_epic)

    parser_tg_time = argparse.ArgumentParser()
    parser_tg_time.add_argument('--time', help='промежуток времени (в секундах), обозначающий интервал, через который будут отправляться фотографии ботом')
    args_time = parser_tg_time.parse_args()
    print(args_time.time)
    try:
        if args_time.time:
            time_stop(args_time.time)
        else:
            time_stop(stop=10)

    except requests.exceptions.HTTPError as error:
        print(error)
