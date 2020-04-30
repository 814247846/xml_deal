import os

from jinja2 import Environment, PackageLoader





class Writer:

    def __init__(self, path, width, height, depth=3, database='Unknown', segmented=0):

        environment = Environment(loader=PackageLoader('pascal_voc_writer', 'templates'), keep_trailing_newline=True)

        self.annotation_template = environment.get_template('annotation.xml')



        abspath = os.path.abspath(path)



        self.template_parameters = {

            'path': abspath,

            'filename': os.path.basename(abspath),

            'folder': os.path.basename(os.path.dirname(abspath)),

            'width': width,

            'height': height,

            'depth': depth,

            'database': database,

            'segmented': segmented,

            'objects': []

        }



    def addObject(self, name, xmin, ymin, xmax, ymax, pose='Unspecified', truncated=0, difficult=0):

        self.template_parameters['objects'].append({

            'name': name,

            'xmin': xmin,

            'ymin': ymin,

            'xmax': xmax,

            'ymax': ymax,

            'pose': pose,

            'truncated': truncated,

            'difficult': difficult,

        })



    def save(self, annotation_path):

        with open(annotation_path, 'w') as file:

            content = self.annotation_template.render(**self.template_parameters)

            file.write(content)





import cv2

import os

import csv



def parse_yolo_labels(images_list_file_name=None, VocLabelsDirReplace=True, classes=[],ret=False):

    with open(images_list_file_name) as f:

        # read one image from list, and add its information

        for line in f:

            # open the txt file, so change the ending of file name to be .txt

            imageFile = str(line.rstrip())

            print(imageFile)

            img = cv2.imread(imageFile)

            height, width, c = img.shape

            #create voc writer

            writer = Writer(imageFile, width=width, height=height)



            # self.filenames.append(imageFile)  only add a file if there are labesl

            current_labels = []

            labelFile = imageFile.replace('jpg', 'txt')

            xmlFile = imageFile.replace('jpg', 'xml')

            if VocLabelsDirReplace:

                labelFile = labelFile.replace('JPEGImages', 'labels')



            with open(labelFile) as csvfile:

                readCSV = csv.reader(csvfile, delimiter=' ')

                for row in readCSV:

                    classID = int(row[0]) + 1  # we add 1 because in ssd 0 is background

                    rectHeight = int(float(row[4]) * height)

                    rectWidth = int(float(row[3]) * width)

                    centerX = row[1] * width

                    centerY = row[2] * height

                    xmin = int(float(row[1]) * width) - int(rectWidth / 2)

                    ymin = int(float(row[2]) * height) - int(rectHeight / 2)

                    xmax = xmin + rectWidth

                    ymax = ymin + rectHeight

                    imageName = os.path.split(imageFile)

                    # imageName = ntpath.basename(imageFile)

                    box = []

                    # box.append(imageName)

                    box.append(classID)

                    box.append(xmin)

                    box.append(ymin)

                    box.append(xmax)

                    box.append(ymax)

                    current_labels.append(box)

                    print(box)

                    # data.append(box)

                    cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 3)

                    writer.addObject(classes[classID], xmin=xmin, ymin=ymin, xmax=xmax, ymax=ymax,difficult=1)

                writer.save(xmlFile)


classes = ['background',"holothurian", "echinus", "scallop","starfish"]


trainFiles = "C:/Yolo/DataSets/3classes/Marana/voc/2012/1/all_2012.txt"

parse_yolo_labels(images_list_file_name=trainFiles,classes=classes)
