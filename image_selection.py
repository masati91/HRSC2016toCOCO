import os
import shutil

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            os.makedirs(directory + "/img")
            os.makedirs(directory + "/gt")
            
    except OSError:
        print ('Error: Creating directory. ' +  directory)
 
def moveImage(directory, index):
    f = open(directory + index.split("_")[-1] + ".txt", 'r')
    lines = f.readlines()

    FullDataSet_path = "FullDataSet/AllImages/"
    file_list = os.listdir(FullDataSet_path)

    for line in lines:
        line = line.strip()
        for file_name in file_list:
            if line == file_name.split(".")[0]:
                shutil.copyfile( FullDataSet_path + file_name, index + "/img/" + file_name)

if __name__ == '__main__':

    folder_list = ["HRSC_train", "HRSC_val"]

    for folder in folder_list:
        createFolder(folder)
        moveImage("ImageSets/", folder)
