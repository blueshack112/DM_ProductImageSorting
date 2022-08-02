import os.path
from typing import List
import pandas as pd
from variales import IMAGES_FOLDER_ROOT, PRODUCT_CSV_PATH


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
        image_paths = crawl_dir(IMAGES_FOLDER_ROOT)


def crawl_dir(dir_root) -> List[str]:
    paths = list()
    for path, subdirs, files in os.walk(dir_root):
        for name in files:
            paths.append(os.path.join(path, name))

    return paths


if __name__ == '__main__':
    main()
