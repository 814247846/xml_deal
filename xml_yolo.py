# 缺陷坐标xml转txt

import xml.etree.ElementTree as ET

classes = ["holothurian", "echinus", "scallop","starfish"]  # 输入缺陷名称，必须与xml标注名称一致

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

img_path= "F:/python/0308/train/image0/"
import cv2
def convert_annotation(image_id):
    in_file = open('F:/python/yanse/label/%s.xml' % (image_id))  # 读取xml文件路径

    out_file = open('F:/python/0308/train/yolo_label/%s.txt' % (image_id), 'w')  # 需要保存的txt格式文件路径
    imgpath = img_path + image_id + ".jpg"
    img = cv2.imread(imgpath)
    imgInfo = img.shape
    h = imgInfo[0]
    w = imgInfo[1]
    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:  # 检索xml中的缺陷名称
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    print(image_id)


image_ids_train = open('F:/python/0308/train/train.txt').read().strip().split()  # 读取xml文件名索引

for image_id in image_ids_train:
    convert_annotation(image_id)




