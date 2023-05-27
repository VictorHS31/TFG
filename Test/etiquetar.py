import os
import cv2 as cv

carpeta_imagenes = "Imagenes"
all_images=os.listdir(carpeta_imagenes)
for imagen in all_images:
    ruta = carpeta_imagenes + "//" + imagen
    print(ruta)
    im = cv.imread(ruta,0)
    print(im)
    cv.imshow("imagen",im)
    cv.waitKey(0)
    valor = str(input("¿Qué numero es?: "))
    if valor != "x" and valor !="X":
        cv.imwrite(os.path.join(carpeta_imagenes,valor + "_" + imagen),im)

for imagen in all_images:
    ruta = carpeta_imagenes + "//" + imagen
    os.remove(ruta)

