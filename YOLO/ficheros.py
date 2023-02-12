import os

directorios = os.listdir()

ruta = "./"
for dir in directorios:
    if dir == "images":
        ruta += dir + "/"
        tipos = os.listdir(ruta)
        for tipo in tipos:
            aux = ruta + tipo + "/"
            print(aux)
            archivos = os.listdir(aux)
            f = open(tipo + ".txt", "w")
            for archivo in archivos:
                if archivo != "classes.txt": f.write(aux + archivo + "\n")
            f.close()
        ruta = "./"
