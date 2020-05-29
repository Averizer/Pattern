import numpy as np # importando numpy
from scipy import stats # importando scipy.stats
import pandas as pd # importando pandas

classes = []

clase1 =([200,210,215,210,198],
        [160,170,172,165,130],
        [120,130,133,134,138])

clase2 = ([90,92,87,91,85],
          [130,138,128,134,123],
          [60,54,66,60,55])

clase3 = ([30,20,24,28,22],
          [44,40,42,50,46],
          [178,180,184,176,181])

cov_c1 = np.cov(np.array(clase1))
cov_c2 = np.cov(np.array(clase2))
cov_c3 = np.cov(np.array(clase3))

print("Matrices de covarianza por clase")
dataframe_cov_c1 = pd.DataFrame(cov_c1, index=["R","G","B"], columns=["c1","",""])
print(dataframe_cov_c1)
print()
dataframe_cov_c2 = pd.DataFrame(cov_c2, index=["R","G","B"], columns=["c2","",""])
print(dataframe_cov_c2)
print()
dataframe_cov_c3 = pd.DataFrame(cov_c3, index=["R","G","B"], columns=["c3","",""])
print(dataframe_cov_c3)

print("Matrices transpuestas por clase")

trans_c1 = np.transpose(clase1)
trans_c2 = np.transpose(clase2)
trans_c3 = np.transpose(clase3)

dataframe_tp_c1 = pd.DataFrame(trans_c1)
print(dataframe_tp_c1)
print()
dataframe_tp_c2 = pd.DataFrame(trans_c2)
print(dataframe_tp_c2)
print()
dataframe_tp_c3 = pd.DataFrame(trans_c3)
print(dataframe_tp_c3)