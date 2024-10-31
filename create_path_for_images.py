import os
import requests
from dotenv import load_dotenv


if not os.path.exists('images'):
    os.makedirs('images')


def create_a_folder_with_photo(file_name, image, image_number, *args):
        response = requests.get(image, *args)
        response.raise_for_status()
        with open(f'images/{file_name}_{image_number}.jpg', 'wb') as file:
            file.write(response.content)


if __name__ == "__main__":
    create_a_folder_with_photo()    
