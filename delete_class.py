import glob
import cv2
import xml.etree.ElementTree as ET
from numpy import *
path = "F:/python/Single-Underwater-Image-Enhancement-and-Color-Restoration-master/train/box1/"
new_path = "F:/python/Single-Underwater-Image-Enhancement-and-Color-Restoration-master/train/box2/"

def write_xml(tree, out_path):
    tree.write(out_path, encoding="utf-8",xml_declaration=True)

for xml_file in glob.glob("{}/*xml".format(path)):
    img_name = xml_file.split("\\")[-1].split('.')[0]
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for i in range(100):
        for object in tree.iter("object"):
            name = str(object.find('name').text)
            if (name in ["waterweeds"]):
                 root.remove(object)
    for object in root.findall('object'):
        name = str(object.find('name').text)
    if not (name in ["holothurian", "echinus", "scallop","starfish"]):
        print(img_name + "------------->label is error--->" + name)
    write_xml(tree, new_path + img_name + ".xml")
    # print("成功处理:{}".format(img_name + ".xml"))


