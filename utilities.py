import pandas as pd
from PIL import Image
import os

def eachRowToYolo(row, imagesFolderPath, nameTxtFile):
    # This function returns an array of matrixes with the form:
    # [[image_name, class, x_center, y_center, width, height]
    #  [image_name, class, x_center, y_center, width, height]
    # ........
    #  [image_name, class, x_center, y_center, width, height]]

    img = Image.open(imagesFolderPath + row['image_name'])
    w = img.width
    h = img.height
    # pute the image name in a txt file
    with open(nameTxtFile, "a") as f:
        f.write(imagesFolderPath + row['image_name'] + "\n")
    if row['BoxesString'] == 'no_box':
        pass
    else:
        matriceList = []
        for i in row['BoxesString'].split(';'):
            xMin, yMin, xMax, yMax = i.split(' ')
            xMin, yMin, xMax, yMax = int(xMin)/h, int(yMin)/h, int(xMax)/w, int(yMax)/w
            lineList = [row['image_name'], 0, (xMin + xMax)/2, (yMin + yMax)/2, xMax - xMin, yMax - yMin]
            matriceList.append(lineList)
        return matriceList


def fromCsvToYolo(csPath, imagesFolderPath, nameTxtFile ,resultsFolderPath):
    """
    This function takes the csv files where each line is an annotation of the format:
    image_name, BoxesString, domain
    and where BoxesString is a string of the format:
    "x_min_1 y_min_1 x_max_1 y_max_1;x_min_2 y_min_2 x_max_2 y_max_2;...;x_min_n y_min_n x_max_n y_max_n"

    Then it creates a series of .txt files, one for each image, where each line is an annotation of the format:
    class_id x_center y_center width height

    It also puts the name of the images in a corresponding txt file by subset

    Parameters
    ----------
    csPath : str
        The path to the csv file
    imagesFolderPath : str
        The path to the folder containing all the images

    Returns
    -------
    None
    """
    data = data = pd.read_csv(csPath)
    matrice = data.apply(eachRowToYolo,
                         nameTxtFile = nameTxtFile,
                         imagesFolderPath = imagesFolderPath,
                         axis=1)
    matrice = matrice.dropna()
    for image in matrice:
        # create a .txt file with the same name as the image
        with open(f"{resultsFolderPath}{image[0][0][:-4]}.txt", "w") as f:
            for box in image:
                f.write(f"{box[1]} {box[2]} {box[3]} {box[4]} {box[5]}\n")

if __name__ == "__main__":
    if not os.path.exists("datasets/wheat2021/labels/"):
        os.makedirs("datasets/wheat2021/labels/")
        
    for i, j in zip(["competition_train.csv", "competition_val.csv", "competition_test.csv"], ["train_txt", "val_txt", "test_txt"]):
        fromCsvToYolo(f"datasets/{i}","datasets/wheat2021/images/", f"datasets/wheat2021/{j[:-4]}.txt", f"datasets/wheat2021/labels/")