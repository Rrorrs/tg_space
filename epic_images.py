import datetime
import requests
import os
from dotenv import load_dotenv
from path_for_images import create_a_folder_with_photo

epic_images = []
def main():
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    return token


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
        epic_url = f'https://api.nasa.gov/EPIC/archive/natural/{change_date}/png/{name_image}.png?api_key={main()}'
        epic_images.append(epic_url)

    for image_number, image in enumerate(epic_images):
        file_name = 'epic_nasa'
        create_a_folder_with_photo(file_name, image, image_number)




if __name__=='__main__':
    
    response_epic = get_image_epic(main())
    get_epic(response_epic)