import requests
from preparation_images import get_picture


HUBBLE_URL = 'http://hubblesite.org/api/v3/image'


def get_image_extension(url):
    image_extension = url.split('.')[-1]
    return image_extension


def fetch_hubble_image(image_id, url=HUBBLE_URL):
    url_images_set = f'{url}/{image_id}'
    response = requests.get(url_images_set)
    response.raise_for_status()
    hubble_image_info = response.json()
    hubble_image_url = f"https:{hubble_image_info['image_files'][-1]['file_url']}"
    filename_hubble_image = f'image_{image_id}.{get_image_extension(hubble_image_url)}'
    get_picture(filename_hubble_image, hubble_image_url)


def fetch_image_id(collection_name, url=HUBBLE_URL):
    url_collection = f'{url}s/{collection_name}'
    headers = {'page': 'all'}
    response = requests.get(url_collection, headers=headers)
    response.raise_for_status()
    collection_info = response.json()
    for objects in collection_info:
        image_id = objects['id']
        fetch_hubble_image(image_id)
