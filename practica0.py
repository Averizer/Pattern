import matplotlib.pyplot as plt
import numpy as np

def sumar(xvector1,yvector1,xvector2,yvector2):
    v1 = len(xvector1)
    v2 = len(xvector2)
    vxResultante = []
    vyResultante = []

    if v1 > v2:
        n = v1 - v2
        for i in range(n):
            xvector2.append(0)

        for i in range(v1):
            vxResultante.append(xvector1[i]+xvector2[i])
            vyResultante.append(yvector1[i]+yvector2[i])
        plt.scatter(vxResultante, vyResultante, label = ('Clase resultante'))
        plt.show()

    
    #if v2 > v1:
    
    #else:


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
op = 0
print ("x por clase:")
print(x_per_class)
while op != 4:

    print("\nAhora que tienes los vectores podemos trabajar con ellos"
         +"\n Digita la opción que desees realizar.")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Salir")
    op = input("Ingresa la opción: ")
    if op == "1":
        v1 = int(input("Selecciona el primer vector a sumar Ci: "))
        v2 = int(input("Selecciona el segundo vector Ci: "))
        sumar(x_per_class[v1],y_per_class[v1],x_per_class[v2],y_per_class[v2])
    if op == "4":
        break







