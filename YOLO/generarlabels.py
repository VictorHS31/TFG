import os
import utils
import shutil

carpeta_imagenes = "./Gas-Meter-Counter/JPEGImages"
carpeta_anotaciones = "./Gas-Meter-Counter/Annotations"
carpeta_anotaciones_digits = "./Gas-Meter-Counter/Annotations_digits"
carpeta_labels = "./Labels"

utils.eliminar(carpeta_imagenes,carpeta_anotaciones,carpeta_anotaciones_digits)

all_images=os.listdir(carpeta_imagenes)
print(f"Total images : {len(all_images)}")

all_anotaciones = os.listdir(carpeta_anotaciones)
print(f"Total annotations : {len(all_anotaciones)}")

all_anotaciones_digits = os.listdir(carpeta_anotaciones_digits)
print(f"Total annotations digits : {len(all_anotaciones_digits)}")

boxes = []
sizes = []
for imagen in all_anotaciones_digits:
  boxes.append(utils.bounding_box(imagen,carpeta_anotaciones_digits))
  sizes.append(utils.get_size(imagen,carpeta_anotaciones))

ruta = carpeta_labels + "/"
for imagen in range(len(boxes)):
  ancho = int(sizes[imagen][0])
  alto = int(sizes[imagen][1])
  nombre = all_anotaciones_digits[imagen].replace(".xml",".txt")
  fichero = open(ruta + nombre, "w")
  for box in range(len(boxes[imagen])):
    digito = boxes[imagen][box]
    xmin = digito[0]
    ymin = digito[1]
    xmax = digito[2]
    ymax = digito[3]
    yolo = utils.normalize_YOLO(ancho,alto,xmin,ymin,xmax,ymax)
    fichero.write(yolo)
  fichero.close()

contador = 0
total = len(os.listdir(carpeta_labels))
ruta = "./Version2/"
for label in os.listdir(carpeta_labels):
  if contador > 0.8 * total:
    shutil.move(carpeta_labels + "/" + label, ruta + "labels/val/" + label)
    imagen = label.replace(".txt",".jpg")
    shutil.move(carpeta_imagenes + "/" + imagen, ruta + "images/val/" + imagen)
  else:
    shutil.move(carpeta_labels + "/" + label, ruta + "labels/train/" + label)
    imagen = label.replace(".txt",".jpg")
    shutil.move(carpeta_imagenes + "/" + imagen, ruta + "images/train/" + imagen)
  contador += 1

utils.generar_ficheros("./Version2/images/")

