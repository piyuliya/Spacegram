from fetch_spacex import fetch_image_spacex_last_launch
from fetch_hubble import fetch_image_hubble

COLLECTOIN_NAME = 'news'


if __name__ == "__main__":
    fetch_image_spacex_last_launch()
    fetch_image_hubble(COLLECTOIN_NAME)
