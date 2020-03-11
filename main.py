from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import fetch_image_id

COLLECTOIN_NAME = 'spacecraft'


if __name__ == "__main__":
    fetch_spacex_last_launch()
    fetch_image_id(COLLECTOIN_NAME)
