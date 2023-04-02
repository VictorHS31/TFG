import os
import pandas as pd

carpeta = os.getcwd() + "\\Analisis\\Resultados\\"
ficheros = os.listdir(carpeta + "ValLoss\\")
total = []

for prueba in ficheros:
    parametros = prueba.split("_")
    prueba = []
    for parametro in parametros:
        if "FILTRO" in parametro or "POOL" in parametro:
            if "FILTROS" not in parametro:
                inicio = parametro.index("(")
                fin = parametro.index(")") + 1
            else:
                inicio = parametro.index("(")
                fin = parametro.index(")")
        else:
            inicio = parametro.index("(")
            fin = parametro.index(")")
        parametro = parametro[inicio + 1:fin]
        prueba.append(parametro)

    for _ in range(4):
        prueba.append(0)
    total.append(prueba)

# Ya tenemos la estructura del csv, ahora falta sacar los diferentes valores
for prueba in total:
    raiz = "ACTIVATION({})_PADDING({})_DROPOUT({})_BALANCEO({})_OPTIMIZADOR({})_FILTRO({})_FILTROS({})_POOL({})_CAPAS-PM({})".format(prueba[0],prueba[1],prueba[2],prueba[3],
                                                                                                                                     prueba[4],prueba[5],prueba[6],prueba[7],prueba[8])
    fichero = pd.read_csv(carpeta + "ValLoss\\" + raiz + "historicoValLoss.txt", header=None)
    indice = fichero.idxmin()
    valor = fichero[0][indice]
    prueba[9] = float(valor)
    fichero = pd.read_csv(carpeta + "TrainLoss\\" + raiz + "historicoTrainLoss.txt", header=None)
    valor = fichero[0][indice]
    prueba[10] = float(valor)
    fichero = pd.read_csv(carpeta + "ValAcc\\" + raiz + "historicoValAcc.txt", header=None)
    valor = fichero[0][indice]
    prueba[11] = float(valor)
    fichero = pd.read_csv(carpeta + "TrainAcc\\" + raiz + "historicoTrainAcc.txt", header=None)
    valor = fichero[0][indice]
    prueba[12] = float(valor)
df = pd.DataFrame(total,
                  columns=["Activation", "Padding", "DropOut", "Balanceo", "Optimizador", "FiltroCNN", "FiltrosCapa", "Pooling", "CapasPM","ValLoss", "TrainLoss", "ValAcc", "TrainAcc"])
df.to_csv("pruebas.csv", index=False)