import datetime
import requests


epic_images = []
def get_epic(response_three, token):
    for block in response_three.json():
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