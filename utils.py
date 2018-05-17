import wget
import shutil
import zipfile
import os

def download_dataset():
    """Download and prepare dataset for training usaging kiwi Challenge structure of data"""

    path_dataset = "./images/FullIJCNN2013.zip"

    # DOWNLOAD DATASET
    print("Downloading ...")
    os.mkdir("./images")
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
    print("\nDeleting object detection image ...")
    list_dataset = os.listdir(path_dataset[:-4])
    for file_name in list_dataset:
        if ".ppm" in file_name:
            os.remove(path_dataset[:-4]+"/"+file_name)

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
    with open(path_dataset[:-4]+"/target.csv", "w") as target:
        target.write("Img_num,classID\n")
        for tag in range(43):

            if tag < 10:
                tag = "0"+str(tag)

            images = os.listdir(path_dataset[:-4]+"/"+str(tag)+"/")

            for img in images:
                target.write(str(img)+","+str(tag)+"\n")
    target.close()
    os.rename(path_dataset[:-4]+"/target.csv","./images/target.csv")


    # PREPARE TRAIN AND TEST DIRECTORY
    print("\nPreparing train and test structure")
    os.mkdir("./images/train")
    os.mkdir("./images/test")

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
    shutil.rmtree(path_dataset[:-4])
