import pandas as pd
from PIL import Image

def from_csv_to_yolo(csv_path, images_folder_path):
    """
    This function takes the csv files where each line is an annotation of the format:
    image_name, BoxesString, domain
    and where BoxesString is a string of the format:
    "x_min_1 y_min_1 x_max_1 y_max_1;x_min_2 y_min_2 x_max_2 y_max_2;...;x_min_n y_min_n x_max_n y_max_n"

    Then it creates a series of .txt files, one for each image, where each line is an annotation of the format:
    class_id x_center y_center width height

    Parameters
    ----------
    csv_path : str
        The path to the csv file
    images_folder_path : str
        The path to the folder containing all the images

    Returns
    -------
    None
    """
