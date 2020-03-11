import requests
from preparation_images import get_picture


SPACE_X_URL = 'https://api.spacexdata.com/v3/launches/latest'


def fetch_spacex_last_launch(url=SPACE_X_URL):
    response = requests.get(url)
    response.raise_for_status()
    latest_launches_info = response.json()
    images_links = latest_launches_info['links']['flickr_images']

    for image_number, image_link in enumerate(images_links):
        filename_image_space_x = f'spacex{image_number}.jpg'
        url_image_space_x = image_link
        get_picture(filename_image_space_x, url_image_space_x)
