import os
import pandas as pd
from matplotlib import pyplot as plt

df_train = pd.read_csv("ACTIVATION(relu)_PADDING(False)_DROPOUT(0.25)_BALANCEO(False)_OPTIMIZADOR(adam)_FILTRO((2, 2))_FILTROS([32, 16])_POOL((2, 2))_CAPAS-PM(3)historicoTrainLoss.txt", header=None)
df_val = pd.read_csv("ACTIVATION(relu)_PADDING(False)_DROPOUT(0.25)_BALANCEO(False)_OPTIMIZADOR(adam)_FILTRO((2, 2))_FILTROS([32, 16])_POOL((2, 2))_CAPAS-PM(3)historicoValLoss.txt", header=None)

print(df_train[0])
print(df_val[0])

plt.plot(df_train[0])
plt.plot(df_val[0])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()