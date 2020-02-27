import matplotlib.pyplot as plt
import numpy as np

xi =[70,75,80,85,90,95,100]
def multiplicar(xvector1,yvector1,xvector2,yvector2):
    vxResultante = []
    vyResultante = []
    v1 = len(xvector1)
    if(len(xvector2)>2 or len(yvector2)>2):
        print("Operación no soprtada.")
    else:
        for i in range(v1):
            vxResultante.append((xvector1[i]*xvector2[0])+(yvector1[i]*xvector2[1]))
            print("Componente calculada "+ str(xvector1[i]) + str(xvector2[0])+str(yvector1[i]) + str(xvector2[1]))
            vyResultante.append((xvector1[i]*yvector2[0])+(yvector1[i]*yvector2[1]))
            print("Componente calculada "+ str(vyResultante))
        print(vxResultante)
        print(vyResultante)
        plt.scatter(vxResultante, vyResultante, label = ('Clase resultante'))
        plt.show()

print("        Hola bienvenid@ al ejercicio 1 Bayesiano simple")
print("Para comenzar ingresa el numero de clases que habrá.")
n_clases = int(input("\tNumero = "))

n_por_clase = 7


print("Cada clase tiene el siguiete numero de características: " + str(n_por_clase))
print("\n\nAhora que tenemos las clases procederemos a llenarlas con las características.")

ft_class = []
classes = []
total_por_clases = 0
total_final = 0
probabilidades_por_clase = []
c = 0
#--------------------------LLenar con los valores -------------------------------

for i in range(n_clases):
    ft_class =[]
    total_por_clases = 0
    for  j in xi:
        features = int(input("Ingresa el numero de incidencias para " + str(j)+ "gr de la clase C"+ str(i) +": "))
        total_por_clases = total_por_clases + 3
        ft_class.append(features)
    classes.append(ft_class)
    total_final = total_final + total_por_clases
    probabilidades_por_clase.append(total_por_clases)

print(total_final)
print(total_por_clases)

for i in range(len(probabilidades_por_clase)):
    aux = probabilidades_por_clase[i]
    probabilidades_por_clase[i] = aux/total_final
    
print(probabilidades_por_clase)


"""
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

#------------------------------Menú----------------------------
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
        print(x_per_class[v1])
        print(y_per_class[v1])
        sumar(x_per_class[v1],y_per_class[v1],x_per_class[v2],y_per_class[v2])
    if op == "2":
        v1 = int(input("Selecciona el primer vector a sumar Ci: "))
        v2 = int(input("Selecciona el segundo vector Ci: "))
        print(x_per_class[v1])
        print(y_per_class[v1])
        restar(x_per_class[v1],y_per_class[v1],x_per_class[v2],y_per_class[v2])
    if op == "3":
        v1 = int(input("Selecciona el primer vector a sumar Ci: "))
        v2 = int(input("Selecciona el segundo vector Ci: "))
        print(x_per_class[v1])
        print(y_per_class[v1])
        multiplicar(x_per_class[v1],y_per_class[v1],x_per_class[v2],y_per_class[v2])
    if op == "4":
        break
"""


