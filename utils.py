import wget
import zipfile
import os

def download_dataset():
    """Download and prepare dataset for training"""

    path_dataset = "./images/FullIJCNN2013.zip"

    # Download Dataset

    # -->print("Downloading ...")
    # -->url = "http://benchmark.ini.rub.de/Dataset_GTSDB/FullIJCNN2013.zip"
    # -->wget.download(url, out=path_dataset)

    # Unzip Dataset

    # -->print("Extracting ..")
    # -->zip_ref = zipfile.ZipFile(path_dataset, 'r')
    # -->zip_ref.extractall("./images/")
    # -->zip_ref.close()

    # Delete FullIJCNN2013.zip

    # -->print("Deleting zip ...")
    # -->os.remove(path_dataset)

    # Delete object detection image

    # -->print("Deleting object detection image ...")
    # -->list_dataset = os.listdir(path_dataset[:-4])
    # -->for file_name in list_dataset:
    # -->    if ".ppm" in file_name:
    # -->        os.remove(path_dataset[:-4]+"/"+file_name)

    # Prepare csv

    # -->print("Preparing csv ...")
    # -->lines = []

    # ClassID and ClassName csv
    # -->with open(path_dataset[:-4]+"/ReadMe.txt", "r") as readme:
    # -->    lines = readme.read().split("\n")
    # -->readme.close()
    # -->lines = lines[-47:-4]

    # -->with open(path_dataset[:-4]+"/class.csv", "w") as classname:
    # -->    classname.write("classID,className\n")
    # -->    for i in lines:
    # -->        classname.write(i.replace("=",",")+"\n")
    # -->classname.close()
    # -->os.rename(path_dataset[:-4]+"/class.csv","./images/class.csv")

    # Image Name and Tag csv
    # -->with open(path_dataset[:-4]+"/target.csv", "w") as target:
    # -->    target.write("Img_num,classID\n")
    # -->    for tag in range(43):

    # -->        if tag < 10:
    # -->            tag = "0"+str(tag)

    # -->        images = os.listdir(path_dataset[:-4]+"/"+str(tag)+"/")

    # -->        for img in images:
    # -->            target.write(str(img)+","+str(tag)+"\n")
    # -->target.close()
    #os.rename(path_dataset[:-4]+"/target.csv","./images/target.csv")


    # Prepare train dir
