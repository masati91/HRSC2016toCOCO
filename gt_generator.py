import os
import shutil
import xml.etree.ElementTree as elemTree

ship_list =[ "ship", "aircraft carrier", "warcraft", "merchant ship", "Nimitz", "Enterprise", "Arleigh Burke", "WhidbeyIsland", "Perry", "Sanantonio",
                "Ticonderoga", "Kitty Hawk", "Kuznetsov", "Abukuma", "Austen", "Tarawa", "Blue Ridge", "Container", "OXo", "Car carrier", "21_none", "Hovercraft",
                "23_none", "yacht", "CntShip", "Cruise", "submarine", "lute", "Medical", "Car carrier2", "Ford-class", "Midway-class", "Invincible-class"]
# len(ship_list) = 31

def generateGt(index):

    img_list = os.listdir(index + "/img")

    FullDataSet_path = "FullDataSet/Annotations/"
    annotation_list = os.listdir(FullDataSet_path)

    for img_name in img_list:
        for annotation in annotation_list:
            if img_name.split(".")[0] == annotation.split(".")[0]:

                tree = elemTree.parse(FullDataSet_path + annotation)
                root = tree.getroot()
                Objects = root.findall("HRSC_Objects")

                for Object in Objects[0].findall("HRSC_Object"):
                    x1 = Object.find("box_xmin").text
                    y1 = Object.find("box_ymin").text
                    x2 = Object.find("box_xmax").text
                    y2 = Object.find("box_ymax").text

                    class_index = int(Object.find("Class_ID").text[-2:])

                    f = open(index + "/gt/gt_"+ img_name.split(".")[0] + ".txt", 'a')
                    f.write(x1 +","+ y1 +","+ x2 +","+ y1 +","+
                            x2 +","+ y2 +","+ x1 +","+ y2 +","+ ship_list[class_index-1] + "\n")

if __name__ == '__main__':

    folder_list = ["HRSC_train", "HRSC_val"]

    for folder in folder_list:
        generateGt(folder)

