import pandas as pd
import matplotlib.pyplot as plt

def visualizacion(parametro):
    df = pd.read_csv("pruebas.csv", encoding="UTF8")
    poblaciones = []
    for poblacion in df[parametro]:
        if poblacion not in poblaciones:
            poblaciones.append(poblacion)
    tamaños = []
    for poblacion in poblaciones:
        aux = df.query("{} == '{}'".format(parametro, poblacion))
        tamaños.append(aux)
    valloss = []
    valacc = []
    for tamaño in tamaños:
        valloss.append(tamaño["ValLoss"])
        valacc.append(tamaño["ValAcc"])
    labels = poblaciones
    fig, ax = plt.subplots()
    ax.boxplot(valloss)
    ax.set_ylabel("Validation Loss")
    ax.set_xticklabels(labels)
    ax.set_title('Comparacion del error de validación en función de ' + parametro)
    ax.yaxis.grid(True)
    plt.savefig('{}boxLoss.png'.format(parametro))
    # plt.show()
    plt.close()
    fig, ax = plt.subplots()
    ax.boxplot(valacc)
    ax.set_ylabel("Validation Accuracy")
    ax.set_xticklabels(labels)
    ax.set_title('Comparacion del accuracy de validación en funcion de ' + parametro)
    ax.yaxis.grid(True)
    plt.savefig('{}boxAcc.png'.format(parametro))
    # plt.show()
    plt.close()


parametros = ["Activation","Padding","DropOut","Balanceo","Optimizador","FiltroCNN","FiltrosCapa","Pooling","CapasPM"]
for parametro in parametros:
    visualizacion(parametro)