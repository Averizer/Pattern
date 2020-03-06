import matplotlib.pyplot as plt
import numpy as np
import math 

xi =[70,75,80,85,90,95,100]
def formula(ev):
    global probabilidades_por_clase
    pre_result = []
    for i in range(len(ev)):
        p = round((math.log(probabilidades_por_clase[i]) + math.log(ev[i])), 3)
        pre_result.append(p)
    
    for i in range(len(pre_result)):
        
        

def closest(ev):
    global xi
    mi = 100000
    close = 0
    
    for i in xi:
        a = i - ev
        aux =  abs(a)
        if(aux <= mi):
            close = i
            mi = aux
    return close

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
#print("Para comenzar ingresa el numero de clases que habrá.")


n_por_clase = 7


print("Cada clase tiene el siguiete numero de características: " + str(n_por_clase))
print("\n\nAhora que tenemos las clases procederemos a llenarlas con las características.")

ft_class = []
classes = []
total_por_clases = []
total_final = 0
probabilidades_por_clase = []
c = 0
c1 = [0,0,1900,300,45,5,0]
c2 = [1800,482,10,8,0,0,0]
c3 = [0,0,0,0,50,400,2000]
#--------------------------LLenar con los valores -------------------------------
classes.append(c1)
classes.append(c2)
classes.append(c3)
print("Las clases son:")
for i in classes:
    print(str(i))
print("")


for i in range (3):
    aux  = 0
    for j in range(7): 
        aux += classes[i][j] 
    probabilidades_por_clase.append(aux)
    total_por_clases.append(aux)
    total_final += aux
    print("El total de la clase es = " + str(aux))

print(total_final)
print(total_por_clases)

#Calculo de probabilidades por clase
for i in range(len(probabilidades_por_clase)):
    aux = probabilidades_por_clase[i]
    probabilidades_por_clase[i] = aux/total_final
    
print("Las probabilidades por clase son: \n "+str(probabilidades_por_clase))

probabilidades = []

for i in range (3):
    aux  = []
    for j in range(7):
        aux.append(round(classes[i][j] / total_por_clases[i], 3))
    probabilidades.append(aux)
    
for i in probabilidades:
    print(str(i))

print("Ahora que tenemos completado el entrenamiento del clasificador" +
      "\n probaremos su funcionamiento.")

op = 0

while op != 2:

    print("\nAhora que tienes los vectores podemos trabajar con ellos"
         +"\n Digita la opción que desees realizar.")
    print("1.- Ingresar una muestra para evaluar")
    print("2.- Salir")

    op = input("Ingresa la opción: ")
    if op == "1":
        x = int(input("Ingresa una muestra: "))
        evaluando = closest(x)
        print("El numero se acerca más a: "+ evaluando)
        
    if op == "2":
        break



