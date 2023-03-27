import xml.etree.ElementTree as ET
import os

def get_digits(image,carpeta):
    bpath = carpeta+"/"+str(image.split(".")[0]+".xml")
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

def bounding_box(image,carpeta):
    bpath = carpeta+"/"+str(image.split(".")[0]+".xml")
    tree = ET.parse(bpath)
    root = tree.getroot()
    objects = root.findall('object')
    boxes = []
    for o in objects:
        bndbox = o.find('bndbox') # reading bound box
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)
        boxes.append([xmin,ymin,xmax,ymax])
    return boxes

def get_size(image,carpeta):
    bpath = carpeta+"/"+str(image.split(".")[0]+".xml")
    tree = ET.parse(bpath)
    root = tree.getroot()
    objects = root.find('size')
    width = objects.find('width').text
    height = objects.find('height').text
    return (width,height)

def normalize_YOLO(width, height, xmin, ymin, xmax,ymax):
    x = (((xmax - xmin) / 2) + xmin) / width
    x = round(x,6)
    y = (((ymax - ymin) / 2) + ymin) / height
    y = round(y,6)
    width_yolo = (xmax - xmin) / width
    width_yolo = round(width_yolo,6)
    height_yolo = (ymax - ymin) / height
    height_yolo = round(height_yolo,6)
    str = "0 {} {} {} {}\n".format(x,y,width_yolo,height_yolo)
    return str

def eliminar(carpeta_imagenes,carpeta_anotaciones,carpeta_anotaciones_digits):
    all_annotations = os.listdir(carpeta_anotaciones)
    all_anotaciones_digits = os.listdir(carpeta_anotaciones_digits)

    for digit in all_annotations:
        if digit not in all_anotaciones_digits:
            os.remove(carpeta_anotaciones + "/" + digit)
            imagen = digit.replace(".xml",".jpg")
            os.remove(carpeta_imagenes + "/" + imagen)
            print("Eliminado: " + carpeta_anotaciones + "/" + digit)
            print("Eliminado: " + carpeta_imagenes + "/" + imagen)

def generar_ficheros(ruta):
    tipos = os.listdir(ruta)
    for tipo in tipos:
        aux = ruta + tipo + "/"
        print(aux)
        archivos = os.listdir(aux)
        f = open("./" + tipo + ".txt", "w")
        for archivo in archivos:
            if archivo != "classes.txt": f.write(aux + archivo + "\n")
        f.close()
        ruta = "./images/"