import math
import os.path
from os import DirEntry
import numpy
import pandas as pd

from variales import IMAGES_FOLDER_ROOT, PRODUCT_CSV_PATH
import sys

sys.setrecursionlimit(10000000)


def main():
    column_conversions = {
        "Images": str
    }
    products_df = pd.read_csv(PRODUCT_CSV_PATH, converters=column_conversions)
    for i, product_row in products_df.iterrows():
        images_str = str(product_row['Images'])
        # if image == numpy.nan:
        if not images_str:
            continue
        images = images_str.split(',')
        image_files = get_image_files(images)
        exit()


def get_image_files(images):
    image_files = list()
    for image in images:
        image_file = find_image_file(image)


def find_image_file(image):
    for path, subdirs, files in os.walk(IMAGES_FOLDER_ROOT):
        for name in files:
            print(os.path.join(path, name))



if __name__ == '__main__':
    main()
