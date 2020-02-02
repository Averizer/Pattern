import matplotlib.pyplot as plt
import numpy as np

print("        Hola bienvenid@ a la practica 0")
print("Para comenzar ingresa el numero de clases que habrá.")
n = int(input("\tNumero = "))

n_por_clase = []
for i in range(n):
    n_por_clase.append( int(input("Ingresa el numero de características para la clase C" + str(i)+" = ")))

print("Cada clase tiene el siguiete numero de características: "+ str(n_por_clase))
print("\n\nAhora que tenemos las clases procederemos a llenarlas con las características.")

c = 0
c2 = 0

arr_aux = []
clases = [][][]

while c < n:
    c2 = n_por_clase[c]
    print("\nClase a registrar características C"+ str(c))
    for x in range(c2):
        x , y = (int(input("Ingresa la caracteristica X"+str(x)+"= ").split()))

        
    c = c+1