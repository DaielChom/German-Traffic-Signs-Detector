import wget
import shutil
import zipfile
import os
import os
from sklearn.linear_model import LogisticRegression
from skimage import io
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.externals import joblib

def download_dataset():
    """Download and prepare dataset for training usaging kiwi Challenge structure of data"""

    path_dataset = "./images/FullIJCNN2013.zip"

    # DOWNLOAD DATASET
    print("Downloading ...")
    os.mkdir("./images",0o777)
    url = "http://benchmark.ini.rub.de/Dataset_GTSDB/FullIJCNN2013.zip"
    wget.download(url, out=path_dataset)

    # UNZIP DATASET
    print("\nExtracting ..")
    zip_ref = zipfile.ZipFile(path_dataset, 'r')
    zip_ref.extractall("./images/")
    zip_ref.close()

    # DELETE FullIJCNN2013.zip
    print("\nDeleting zip ...")
    os.remove(path_dataset)

    # DELETE OBJECT DETECTION IMAGE
    #print("\nDeleting object detection image ...")
    #list_dataset = os.listdir(path_dataset[:-4])
    #for file_name in list_dataset:
    #    if ".ppm" in file_name:
    #        os.remove(path_dataset[:-4]+"/"+file_name)

    # PREPARE CSV
    print("\nPreparing csv ...")
    lines = []

    # ClassID and ClassName csv
    with open(path_dataset[:-4]+"/ReadMe.txt", "r") as readme:
        lines = readme.read().split("\n")
    readme.close()
    lines = lines[-47:-4]

    with open(path_dataset[:-4]+"/class.csv", "w") as classname:
        classname.write("classID,className\n")
        for i in lines:
            classname.write(i.replace("=",",")+"\n")
    classname.close()
    os.rename(path_dataset[:-4]+"/class.csv","./images/class.csv")

    # Image Name and Tag csv
    #with open(path_dataset[:-4]+"/target.csv", "w") as target:
    #    target.write("Img_num,classID\n")
    #    for tag in range(43):

    #        if tag < 10:
    #            tag = "0"+str(tag)

    #        images = os.listdir(path_dataset[:-4]+"/"+str(tag)+"/")

    #        for img in images:
    #            target.write(str(tag)+str(img)+","+str(tag)+"\n")
    #target.close()
    #os.rename(path_dataset[:-4]+"/target.csv","./images/target.csv")


    # PREPARE TRAIN AND TEST DIRECTORY
    print("\nPreparing train and test structure")
    os.mkdir("./images/train/",0o777)
    os.mkdir("./images/test/", 0o777)

    for tag in range(43):
        if tag < 10:
            tag = "0"+str(tag)

        # select 80% per class for train and 20% per class for test
        images = len(os.listdir(path_dataset[:-4]+"/"+str(tag)+"/"))
        per_80 = round(images*0.8)
        per_20 = round(images*0.2)
        # DUDA
        # Que tan obligatorio es que en test haya imagenes con todas las clases
        if(per_20) == 0:
            per_80 = 1
            per_20 = 1
        # DUDA
        train_tag = os.listdir(path_dataset[:-4]+"/"+str(tag)+"/")[:per_80]
        test_tag = os.listdir(path_dataset[:-4]+"/"+str(tag)+"/")[per_80:]

        # move image to train and test
        for file_train in train_tag:
            os.rename(path_dataset[:-4]+"/"+str(tag)+"/"+file_train, "./images/train/"+str(tag)+file_train)

        for file_test in test_tag:
            os.rename(path_dataset[:-4]+"/"+str(tag)+"/"+file_test, "./images/test/"+str(tag)+file_test)

    # TRAIN AND TEST TARGET CSV
    PATH_TRAIN = "./images/train/"
    PATH_TEST = "./images/test/"

    # train target
    with open("./images/target_train.csv", "w") as target_train:
        target_train.write("imgName,classID\n")

        images = os.listdir(PATH_TRAIN)

        for img in images:
            target_train.write(img+","+img[:2]+"\n")
    target_train.close()

    # test target
    with open("./images/target_test.csv", "w") as target_test:
        target_test.write("imgName,classID\n")

        images = os.listdir(PATH_TEST)

        for img in images:
            target_test.write(img+","+img[:2]+"\n")
    target_test.close()

    # DELETE FILES
    shutil.rmtree(path_dataset[:-4])


def get_RGB_flatten(img):
    """Concatenate flatten channels of a image"""
    image = np.array(img)
    R = image[:,:,0].flatten()
    G = image[:,:,1].flatten()
    B = image[:,:,2].flatten()

    return list(R)+list(G)+list(B)

def get_all_images(PATH):
    """Return a list with all image resized of a path especific"""
    temp_list = []
    maxsize = (128, 128)
    dir_list = os.listdir(PATH)
    for i in dir_list:
        temp_list.append(Image.open(PATH+i).resize(maxsize, Image.ANTIALIAS))
    return temp_list

def logistic_regression_scikit_learn():
    """Train logistic regression with scikit-learn framework"""

    print("Training ...")


    PATH_TRAIN = "./images/train/"
    train_image = get_all_images(PATH_TRAIN)

    train_RGB = []
    for i in train_image:
        train_RGB.append(get_RGB_flatten(i))

    target_train = pd.read_csv("images/target_train.csv")

    train_y = []
    for i in target_train.values:
        train_y.append(i[1])

    lg = LogisticRegression()
    lg.fit(train_RGB,train_y)

    print("Saving model ...")
    joblib.dump(lg, './models/model1/saved/logistic-Regression-sckit-learn.pkl')


def select_train_model(model_name):
    """Switch between the different model"""
    if model_name == "LRSL":
        logistic_regression_scikit_learn()

    else:
        print("Model not found")
