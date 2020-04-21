import requests
import os
import logging
import PIL
from PIL import Image, ImageFile
from pathlib import Path
from upload import upload_photo


DIR_NAME = "images"
Path(DIR_NAME).mkdir(parents=True, exist_ok=True)

ImageFile.LOAD_TRUNCATED_IMAGES = True

logging.basicConfig(filename='app.log', filemode='w')


def save_picture(filename, url, name_dir=DIR_NAME):
    file_path = os.path.join(name_dir, filename)
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)
    return filename


def crop_image(image_name):
    try:
        image = Image.open(f'images/{image_name}')
        if image.width > image.height:
            delta_left = int((image.width - image.height)/2)
            delta_right = int(image.width - delta_left)
            coordinates = (delta_left, 0, delta_right, image.height)
            cropped = image.crop(coordinates)
            cropped.save(f'images/{image_name}')
            return image_name
        else:
            delta_left = int((image.height - image.width)/2)
            delta_right = int(image.height - delta_left)
            coordinates = (0, delta_left, image.width, delta_right)
            cropped = image.crop(coordinates)
            cropped.save(f'images/{image_name}')
            return image_name
    except PIL.UnidentifiedImageError:
        logging.exception('cannot identify image file')


def post_image_in_instagram(filename, url):
    filename_for_crop_image = save_picture(filename, url)
    image_name_for_upload = crop_image(filename_for_crop_image)
    upload_photo(image_name_for_upload)
