import time
import settings
from instabot import Bot
from preparation_images import logging

bot = Bot()
bot.login(username=settings.LOGIN, password=settings.PASSWORD)


def upload_photo(image_name):
    try:
        bot.upload_photo(f'images/{image_name}', caption="Nice pic!")
        time.sleep(60)
    except Exception as e:
        logging.exception(e)
