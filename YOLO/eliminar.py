carpeta_imagenes = "./Gas-Meter-Counter/JPEGImages"
carpeta_anotaciones = "./Gas-Meter-Counter/Annotations"
carpeta_anotaciones_digits = "./Gas-Meter-Counter/Annotations_digits"

import numpy as np # linear algebra
import xml.etree.ElementTree as ET # for parsing XML
from PIL import Image # to read images
import os
import glob
import cv2 as cv
from matplotlib import pyplot as plt
import uuid
import time

all_images = os.listdir(carpeta_imagenes)
all_annotations = os.listdir(carpeta_anotaciones)
all_annotations_digits = os.listdir(carpeta_anotaciones_digits)

for digit in all_annotations:
    if digit not in all_annotations_digits:
        os.remove(carpeta_anotaciones + "/" + digit)
        imagen = digit.replace(".xml",".jpg")
        os.remove(carpeta_imagenes + "/" + imagen)
        print("Eliminado: " + carpeta_anotaciones + "/" + digit)
        print("Eliminado: " + carpeta_imagenes + "/" + imagen)



