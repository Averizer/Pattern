import matplotlib.pyplot as plt
import numpy as np
import math as m


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

plt.legend()
plt.show()
#---------------------- Calcular distancias ---------------------------
distancias_por_clase = []


def calcular_distancia(muestra, k, op):
    global n
    global classes
    global distancias_por_clase
    c=0
    if op == "1":
        
        while  c < n:
            caux = n_por_clase[c]
            aux = []
            res = ((muestra[0]-x_centroide_por_clase[c])**2) + ((muestra[1]-y_centroide_por_clase[c])**2)
            res = m.sqrt(res)
            aux.append(res)
            distancias_por_clase.append(aux)
            xaxis = [aux]
            c = c+1
        print("Distancias")
        print(distancias_por_clase)
    if op == "2":
        while  c < n:
            caux = n_por_clase[c]
            aux = []
            for x in range(caux):
                res = ((muestra[0]-classes[c][x][0])**2) + ((muestra[1]-classes[c][x][1])**2)
                res = m.sqrt(res)
                aux.append(res)
            distancias_por_clase.append(aux)
            xaxis = [aux]
            c = c+1
        print("Distancias")
        print(distancias_por_clase)
    #+++++++++++++++++++++++++++++ Evauluar distancia ++++++++++++++++++++
    c = 0
    distancias_finales = []
    while  c < n:
        distancias_por_clase[c].sort()
        distancias_finales.append(np.sum(distancias_por_clase[c][0:k]))
        c += 1
    distMin = min(distancias_finales)
    
    print("La distancia total minima pertenerce a la clase C{}".format(distancias_finales.index(distMin)))
    print("Las distancias totales separadas por clase son: ")
    print(distancias_finales, end="\n\n")


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

#----------------------------- Menú -----------------------------------
op = 0
while op != 2:
    print("\nAhora que tienes los vectores podemos trabajar con ellos"
         +"\n Digita la opción que desees realizar.")
    print("1.- Ingresar una muestra ")
    print("2.- Salir")
    op = input("Ingresa la opción: ")
    if op == "1":
        print("¿Calcular por centroide o clase completa?")
        print("1.- Centroide ")
        print("2.- Clase completa ")
        op2 = input("Ingresa la opción: ")
        if op2 == "1":
            muestra = list(map(float, input("Ingresa una coordenada a evaluar (digitos) separadas por Espacio ").split()))
            print("Para cauntos vecinos k quieres evaluar? (k) /n No puedes ser mas de {}".format(max(n_por_clase)))
            k = int(input("K= " ))
            print("Todos los calculos serán basados en la distancia eulidea")
            calcular_distancia(muestra, k, op2)
        
        if op2 == "2":
            muestra = list(map(float, input("Ingresa una coordenada a evaluar (digitos) separadas por Espacio ").split()))
            print("Para cauntos vecinos k quieres evaluar? (k) /n No puedes ser mas de {}".format(max(n_por_clase)))
            k = int(input("K= " ))
            print("Todos los calculos serán basados en la distancia eulidea")
            calcular_distancia(muestra, k, op2)
        
    if op == "2":
        break