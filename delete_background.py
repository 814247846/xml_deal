import glob
import cv2
import os
import xml.etree.ElementTree as ET
from numpy import *
path = "F:/python/Single-Underwater-Image-Enhancement-and-Color-Restoration-master/train/box4/"
imgpath = "F:/python/Single-Underwater-Image-Enhancement-and-Color-Restoration-master/train/image/"
i =0
for xml_file in glob.glob("{}/*xml".format(path)):

    img_name = xml_file.split("\\")[-1].split('.')[0]
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for object in root.findall('object'):
        name = str(object.find('name').text)
    if root.findall('object')==[]:
        i = i+1
        os.remove(path + img_name+".xml")
        if os._exists(imgpath + img_name + ".jpg"):
            os.remove(imgpath + img_name + ".jpg")
print(i)




