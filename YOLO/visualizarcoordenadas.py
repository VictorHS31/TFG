import os
import utils
import cv2 as cv

carpeta_imagenes = "./Gas-Meter-Counter/JPEGImages"
carpeta_anotaciones_digits = "./Gas-Meter-Counter/Annotations_digits"
carpeta_anotaciones = "./Gas-Meter-Counter/Annotations"

all_images=os.listdir(carpeta_imagenes)
all_anotaciones_digits = os.listdir(carpeta_anotaciones_digits)

boxes = []
sizes = []
for imagen in all_anotaciones_digits:
  boxes.append(utils.bounding_box(imagen,carpeta_anotaciones_digits))
  sizes.append(utils.get_size(imagen,carpeta_anotaciones))

for imagen in range(len(boxes)):
  ancho = int(sizes[imagen][0])
  alto = int(sizes[imagen][1])
  img = cv.imread(carpeta_imagenes + "/" + all_images[imagen])
  for box in range(len(boxes[imagen])):
    digito = boxes[imagen][box]
    xmin = digito[0]
    ymin = digito[1]
    xmax = digito[2]
    ymax = digito[3]
    img = cv.rectangle(img, (xmin, ymin),(xmax, ymax),(0,0,255),2)
  cv.imshow(all_images[imagen],img)
  cv.waitKey(50000)
  break
