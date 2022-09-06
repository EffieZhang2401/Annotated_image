import os
import cv2 as cv
import re
import xml.etree.ElementTree as ET
from tqdm import tqdm
def annotatedImg(inputPath, outputPath):
    #xmlPath and imgPath are set of the string of xml paths and png paths
    imagelist = os.listdir(inputPath)
    for image in tqdm(imagelist):
        if image.find('DS_Store')!=-1 or image.find('xml') != -1:
            continue
        image_pre, ext = os.path.splitext(image)
        
        img_file = inputPath + "/" + image
        xml_file = inputPath + "/" + image_pre + '.xml'
        output_file = outputPath + "/" + image

        img = cv.imread(img_file)

        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Stack to store all the nodes of tree
        s1 = []
 
        # Stack to store all the leaf nodes
        s2 = []
 
        s1.append(root)
        while len(s1) != 0:
            curr = s1.pop()
            if len(curr)>0:
                for child in curr:
                    s1.append(child)
 
            # If current node is a leaf node push it onto the second stack
            else:
                #print('yes')
                #print(curr.tag, curr.attrib)
                s2.append(curr)

        for node in s2:
            bndbox = node.attrib.get('bounds')
            xycord = re.split(',|\[|\]', bndbox)
            x1 = int(xycord[1])
            y1 = int(xycord[2])
            x2 = int(xycord[4])
            y2 = int(xycord[5])
            cv.rectangle(img,(x1,y1),(x2,y2),(0, 255, 255),3)
            cv.imwrite(output_file, img)
            #print(x1,y1,x2,y2)
        

annotatedImg('input', 'output')

