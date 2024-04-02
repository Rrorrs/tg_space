import requests


days = []
def add_day_images(response_two):
    for block in response_two.json():
        day_images = block['url']
        days.append(day_images)

    for image_number, image in enumerate(days):
        response = requests.get(image)
        response.raise_for_status()
        with open(f'images/nasa_apod_{image_number}.jpg', 'wb') as file:
            file.write(response.content)