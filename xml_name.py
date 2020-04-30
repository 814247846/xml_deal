import glob
import cv2
import xml.etree.ElementTree as ET
from numpy import *
path = "./annotations1/"
new_path = "./annotations/"

def write_xml(tree, out_path):
    tree.write(out_path, encoding="utf-8",xml_declaration=True)

for xml_file in glob.glob("{}/*xml".format(path)):
    img_name = xml_file.split("\\")[-1].split('.')[0]
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for object in root.findall('object'):
        name = str(object.find('name').text)
        if name =="0":
            object.find('name').text="holothurian"
        elif name =="1":
            object.find('name').text = "echinus"
        elif name =="2":
            object.find('name').text = "scallop"
        elif name =="3":
            object.find('name').text = "starfish"
    # if not (name in ["holothurian", "echinus", "scallop","starfish"]):
    #     print(img_name + "------------->label is error--->" + name)
    write_xml(tree, new_path + img_name + ".xml")
    print("成功处理:{}".format(img_name + ".xml"))


