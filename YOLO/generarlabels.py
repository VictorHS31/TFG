carpeta_imagenes = "./Gas-Meter-Counter/JPEGImages"
carpeta_anotaciones = "./Gas-Meter-Counter/Annotations"
carpeta_anotaciones_digits = "./Gas-Meter-Counter/Annotations_digits"

import xml.etree.ElementTree as ET
import os
import cv2 as cv
from matplotlib import pyplot as plt


all_images=os.listdir(carpeta_imagenes)
print(f"Total images : {len(all_images)}")

all_anotaciones = os.listdir(carpeta_anotaciones)
print(f"Total annotations : {len(all_anotaciones)}")

all_anotaciones_digits = os.listdir(carpeta_anotaciones_digits)
print(f"Total annotations digits : {len(all_anotaciones_digits)}")


def get_digits(image):
    bpath=carpeta_anotaciones_digits+"/"+str(image.split(".")[0]+".xml")
    try:
      tree = ET.parse(bpath)
    except:
      return []
    root = tree.getroot()
    objects = root.findall('object')
    
    digits = []
    for o in objects:
        name = o.find('name').text # reading bound box
        digits.append(name)
    return digits

def bounding_box(image):
    bpath=carpeta_anotaciones+"/"+str(image.split(".")[0]+".xml")
    tree = ET.parse(bpath)
    root = tree.getroot()
    objects = root.findall('object')
    
    for o in objects:
        bndbox = o.find('bndbox') # reading bound box
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)
        print(o)
        
    print(xmin,ymin,xmax,ymax)
    return (xmin,ymin,xmax,ymax)

