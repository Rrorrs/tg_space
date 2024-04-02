import requests


def fetch_spacex_last_launch(images):
    for image_number, image in enumerate(images):
        response = requests.get(image)
        response.raise_for_status()
        with open(f'images/spacex_{image_number}.jpg', 'wb') as file:
            file.write(response.content)