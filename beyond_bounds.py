import glob
import cv2
import xml.etree.ElementTree as ET
from numpy import *

import numpy as np
path = "F:/python/Single-Underwater-Image-Enhancement-and-Color-Restoration-master/train/box/"
new_path = "F:/python/Single-Underwater-Image-Enhancement-and-Color-Restoration-master/train/box1/"

img_path = "F:/python/Single-Underwater-Image-Enhancement-and-Color-Restoration-master/train/image/"


def write_xml(tree, out_path):
    tree.write(out_path, encoding="utf-8",xml_declaration=True)
for xml_file in glob.glob("{}/*xml".format(path)):
    img_name = xml_file.split("\\")[-1].split('.')[0]
    imgpath = img_path + img_name + ".jpg"
    img = cv2.imread(imgpath)
    imgInfo = img.shape
    height = imgInfo[0]
    width = imgInfo[1]
    tree = ET.parse(xml_file)
    root = tree.getroot()
    obnode = root.findall("object")
    for node in obnode:
        boxnode = node.findall("bndbox")
        for node in boxnode:
            xminnode = node.findall("xmin")
            for node in xminnode:
                if int(node.text) < 0:
                    node.text =str(0)
        for node in boxnode:
            xmaxnode = node.findall("xmax")
            for node in xmaxnode:
                if int(node.text) >width:
                    node.text =str(width-1)
        for node in boxnode:
            yminnode = node.findall("ymin")
            for node in yminnode:
                if int(node.text) < 0:
                    node.text =str(0)
        for node in boxnode:
            ymaxnode = node.findall("ymax")
            for node in ymaxnode:
                if int(node.text) >height:
                    node.text =str(height-1)
    write_xml(tree, new_path+img_name+".xml")
    print("成功处理:{}".format(img_name+".xml"))


