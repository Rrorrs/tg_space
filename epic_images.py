import datetime
import requests
import os
from dotenv import load_dotenv
load_dotenv()


token = os.environ['TOKEN']
epic_images = []


def get_image_epic(token):
    epic_link = "https://api.nasa.gov/EPIC/api/natural/image"
    params = {
            "api_key": token
        }

    response = requests.get(epic_link, params=params)
    response.raise_for_status()
    return response


def get_epic(response_epic):
    for block in response_epic.json():
        name_image = block['image']
        date_image = block['date']
        date_=datetime.datetime.strptime(date_image, '%Y-%m-%d %H:%S:%M')
        date = datetime.datetime.date(date_)
        date = str(date)
        change_date = date.replace('-', '/')
        epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{change_date}/png/{name_image}.png?api_key={token}'
        epic_images.append(epic_url)

    for image_number, image in enumerate(epic_images):
        response = requests.get(image)
        response.raise_for_status()
        with open(f'images/nasa_epic_{image_number}.png', 'wb') as file:
            file.write(response.content)


