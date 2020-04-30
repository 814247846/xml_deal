import glob
import cv2
import xml.etree.ElementTree as ET
from numpy import *
path = "F:/python/Single-Underwater-Image-Enhancement-and-Color-Restoration-master/train/box2/"
new_path = "F:/python/Single-Underwater-Image-Enhancement-and-Color-Restoration-master/train/box3/"

def write_xml(tree, out_path):
    tree.write(out_path, encoding="utf-8",xml_declaration=True)
count = 0
for xml_file in glob.glob("{}/*xml".format(path)):

    img_name = xml_file.split("\\")[-1].split('.')[0]
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for i in range(100):
        for object1 in tree.iter("object"):
            object = object1.find("bndbox")
            xmin= int(object.find('xmin').text)
            xmax = int(object.find('xmax').text)
            ymin = int(object.find('ymin').text)
            ymax = int(object.find('ymax').text)
            if ((xmin>xmax) or (ymin>ymax) or (abs(ymax-ymin)*abs(xmax-xmin)<=20)):
                 # print(img_name)
                 # print("xmin{}".format(xmin))
                 # print("xmax{}".format(xmax))
                 # print("ymin{}".format(ymin))
                 # print("ymax{}".format(ymax))
                 root.remove(object1)
                 count=count+1
    for object in root.findall('object'):
        name = str(object.find('name').text)
    if not (name in ["holothurian", "echinus", "scallop","starfish"]):
        print(img_name + "------------->label is error--->" + name)
    write_xml(tree, new_path + img_name + ".xml")

    # print("成功处理:{}".format(img_name + ".xml"))
print("删除{}".format(count))


