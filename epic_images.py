import datetime
import requests
import os
from dotenv import load_dotenv
from create_path_for_images import save_photo_in_folder


def get_image_epic(token):
    epic_link = "https://api.nasa.gov/EPIC/api/natural/image"
    params = {
            "api_key": token
        }

    response = requests.get(epic_link, params=params)
    response.raise_for_status()
    return response


def get_epic(response_epic):
    epic_images = []
    for block in response_epic.json():
        name_image = block['image']
        date_image = block['date']
        date_=datetime.datetime.strptime(date_image, '%Y-%m-%d %H:%S:%M')
        date = datetime.datetime.date(date_)
        date = str(date)
        changed_date = date.replace('-', '/')
        payload = {'api_key': f'{token}'}
        epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{changed_date}/png/{name_image}.png'
        epic_images.append(epic_url)

    for image_number, image_link in enumerate(epic_images):
        file_name = 'epic_nasa'
        save_photo_in_folder(file_name, image_link, image_number, payload)




if __name__=='__main__':
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    response_epic = get_image_epic(token)
    get_epic(response_epic)