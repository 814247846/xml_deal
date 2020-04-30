import glob
import cv2
import xml.etree.ElementTree as ET
from numpy import *
path = "F:/python/Single-Underwater-Image-Enhancement-and-Color-Restoration-master/train/box4/"

def write_xml(tree, out_path):
    tree.write(out_path, encoding="utf-8",xml_declaration=True)
count = 0
h=0
e=0
s=0
st=0

for xml_file in glob.glob("{}/*xml".format(path)):

    img_name = xml_file.split("\\")[-1].split('.')[0]
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for object in root.findall('object'):
        name = str(object.find('name').text)
        if name =="holothurian":
            h=h+1
        if name == "echinus":
            e = e + 1
        if name == "scallop":
            s =s+1
        if name == "starfish":
            st = st+1
print(h,e,s,st)
