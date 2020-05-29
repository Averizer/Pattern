import matplotlib.pyplot as plt
import numpy as np
import math as m

def calcularCB(muestra):
    global x_centroide_por_clase
    global y_centroide_por_clase
    c = len(x_centroide_por_clase)
    distanciascb  = []
    
    #--------------------City Block---------------
    for i in range(x_centroide_por_clase):
        cb = abs(x_centroide_por_clase[i] - muestra[0]) + abs(y_centroide_por_clase[i] - muestra[1])
        distanciascb.append(cb)
    
    imprimircentroides(muestra)
    print("La distancia mas cercana es: ")
    print(min(distanciascb))
    print("Pertenece a la clase "+ distanciascb.index(min(distanciascb)))
    pass

def calcularE(muestra):
    global x_centroide_por_clase
    global y_centroide_por_clase
    c = len(x_centroide_por_clase)
    distanciascb  = []
    distanciase = []
    #--------------------Euclideae----------------
    for i in range(x_centroide_por_clase):
        e = m.sqrt(((x_centroide_por_clase[i] - muestra[0])**2)+((y_centroide_por_clase[i] - muestra[1])**2)) 
        distanciase.append(e)
    imprimircentroides(muestra)
    print("La distancia mas cercana es: ")
    print(min(distanciase))
    print("Pertenece a la clase "+ distanciase.index(min(distanciase)))
    pass

def calcularM(muestra):
    global x_centroide_por_clase
    global y_centroide_por_clase
    c = len(x_centroide_por_clase)
    distanciascb  = []
    distanciase = []
    #--------------------Euclideae----------------
    for i in range(x_centroide_por_clase):
        e = m.sqrt(((x_centroide_por_clase[i] - muestra[0])**2)+((y_centroide_por_clase[i] - muestra[1])**2)) 
        distanciase.append(e)
    imprimircentroides(muestra)
    pass

print("        Hola bienvenid@ a la practica ")
print("Para comenzar ingresa el numero de clases que habrá.")
n = int(input("Numero = "))
n_por_clase = []

for i in range(n):
    n_por_clase.append( int(input("Ingresa el numero de características para la clase C" + str(i)+" = ")))

print("Cada clase tiene el siguiete numero de características: "+ str(n_por_clase))
print("\n\nAhora que tenemos las clases procederemos a llenarlas con las características.")

c = 0
clases = []
arr_aux = []
clases = []
ft_class = []
classes = []
#--------------------Llenar clases-------------------------------------
while c < n:
    c2 = n_por_clase[c]
    print("\nClase a registrar características C"+ str(c))
    ft_class = []
    for x in range(c2):
        features = list(map(int, input("Ingresa (X"+str(x)+"), coordenadas (digitos) separadas por Espacio ").split()))
        ft_class.append(features)
    classes.append(ft_class)
    c = c+1
    
    
print(classes)
c=0 
xaxis = []
yaxis = []
x_per_class =[]
y_per_class =[]

#---------------------Imprimir clases---------------------------------
while c < n:
    c2 = n_por_clase[c]
    for x in range(c2):
        xaxis.append(classes[c][x][0])
        yaxis.append(classes[c][x][1])
    plt.scatter(xaxis, yaxis, label = ('Clase C'+ str(c)))
    x_per_class.append(xaxis)
    y_per_class.append(yaxis)
    xaxis = []
    yaxis = []
    c = c+1
    
plt.title("Clases")
plt.xlabel("Característica x")
plt.ylabel("Característica y")
plt.legend()
plt.show()

print("x and y per class")
print(x_per_class)
print(y_per_class)
#---------------------Calcular centroides-------------------------------
x_centroide_por_clase = []
y_centroide_por_clase = []

l = len(x_per_class)
for c in range(n):
    aux_x = 0
    aux_y = 0
    for i in range(2):
        aux_x += x_per_class[c][i]
        aux_y += y_per_class[c][i]
    print(aux_x)
    print(aux_y)
    x_centroide_por_clase.append(aux_x/l)
    y_centroide_por_clase.append(aux_y/l)
    c = c + 1

#---------------------Imprimir centroides---------------------------------
for co in range(len(x_centroide_por_clase)):
    plt.scatter(x_centroide_por_clase[co], y_centroide_por_clase[co], label = ('Centroide de la Clase C'+ str(co)))
    xaxis = []
    yaxis = []

def imprimircentroides(muestra):
    global x_centroide_por_clase
    global y_centroide_por_clase
    for co in range(len(x_centroide_por_clase)):
        plt.scatter(x_centroide_por_clase[co], y_centroide_por_clase[co], label = ('Centroide de la Clase C'+ str(co)))
        xaxis = []
        yaxis = []
    plt.scatter(muestra[0], muestra[1], label = ("Muestra"))
    plt.legend()
    plt.show()
    pass

print("Centroides:")
print(x_centroide_por_clase)
print(y_centroide_por_clase)

plt.legend()
plt.show()

op = 0
print ("x por clase:")
print(x_per_class)

#----------------Menú-----------------------
while op != 2:
    print("\nAhora que tienes los vectores podemos trabajar con ellos"
         +"\n Digita la opción que desees realizar.")
    print("1.- Ingresar una muestra ")
    print("2.- Salir")
    op = input("Ingresa la opción: ")
    if op == "1":
        muestra = list(map(float, input("Ingresa una coordenada a evaluar (digitos) separadas por Espacio ").split()))
        print("Ahora selecciona que distancia quieres calcular")
        print("1.- Distancia City Block")
        print("2.- Distancia Euclidea")
        print("3.- Distancia Mahalanobis")
        distancia = int(input("Ingresa seleccion"))
        if distancia == 1:
            calcularCB(muestra);
        if distancia == 2:
            calcularE(muestra);
        if distancia == 3:
            calcularM(muestra);
        break
    if op == "2":
        break
