import requests
import os
from preparation_images import post_image_in_instagram


HUBBLE_URL = 'http://hubblesite.org/api/v3/image'


def get_image_extension(url):
    image_extension = os.path.splitext(url)[1]
    print(image_extension)
    return image_extension


def fetch_hubble_image_data(image_id, url=HUBBLE_URL):
    url_images_set = f'{url}/{image_id}'
    response = requests.get(url_images_set)
    response.raise_for_status()
    hubble_image_info = response.json()
    url_hubble_image = f"https:{hubble_image_info['image_files'][-1]['file_url']}"
    filename_hubble_image = f'image_{image_id}{get_image_extension(url_hubble_image)}'
    post_image_in_instagram(filename_hubble_image, url_hubble_image)


def fetch_image_hubble(collection_name, url=HUBBLE_URL):
    url_collection = f'{url}s/{collection_name}'
    headers = {'page': 'all'}
    response = requests.get(url_collection, headers=headers)
    response.raise_for_status()
    collection_info = response.json()
    for objects in collection_info:
        image_id = objects['id']
        fetch_hubble_image_data(image_id)
