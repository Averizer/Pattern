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

ft_class = []
classes = []
c = 0

while c < n:
    c2 = n_por_clase[c]
    print("\nClase a registrar características C"+ str(c))
    ft_class = []
    for x in range(c2):
        features = list(map(int, input("Ingresa (X"+str(x)+"), coordenadas separadas por Espacio ").split()))
        ft_class.append(features)
    classes.append(ft_class)
    c = c+1

print(classes)
c=0 
xaxis = []
yaxis = []
while c < n:
    c2 = n_por_clase[c]
    for x in range(c2):
        xaxis.append(classes[c][x][0])
        yaxis.append(classes[c][x][1])
    plt.plot(xaxis, yaxis, label = ('Clase C'+ str(c)))
    print(xaxis)
    print(yaxis)
    xaxis = []
    yaxis = []
    c = c+1
    
plt.title("Clases")
plt.xlabel("x coordinate")
plt.ylabel("y coordinate")
plt.legend()
plt.show()