from pylab import *
import numpy as np
#from tabulate import tabulate
import math
from time import sleep

def bayesiano_simple():
    print("\nOpcion 1 - Bayesiano Simple")
    nombre_clase = input("¿Que es lo que vas a clasificar?\n")
    clase = []
    num_patron = int(input("¿Cuantas clases va a introducir? : "))
    i = 0
    muestra_total = 0
    while i < num_patron:
        nombre_patron = input("Nombre de la clase: ")
        muestra_patron = int(input("Cual es la muestra de la clase: "))
        muestra_total = muestra_total + muestra_patron
        patron = Patron(nombre_patron, muestra_patron)
        clase.append(patron)
        i += 1
    rasgo_nombre = input("¿Que rasgo va a ocuparse? (debe ser medible el rasgo) : ")
    rasgo_min = float(input("Numero minimo del rango del rasgo: "))
    rasgo_max = float(input("Numero maximo del rango del rasgo: "))
    num_variaciones = float(input("Numero de variaciones: "))
    rango = rasgo_max - rasgo_min
    num_v = rango / (num_variaciones-1)
    min = rasgo_min
    i = 0
    j = 0
    variaciones = []
    muestras_total = []
    while min <= rasgo_max:
        variaciones.append(min)
        muestras = []
        while i < len(clase):

            print("\n\nMuestras en las variaciones de la clase ", clase[i].nombre, "\n")
            print("Se recuerda que la clase ", clase[i].nombre, " tiene un tamaño maximo de ", clase[i].muestra)
            muestras_r = clase[i].muestra
            print("De la variacion ",min ," :")
            muestra_variacion = int(input("Cual es el tamaño de muestra: "))
            if muestra_variacion > muestras_r:
                print("El tamaño introducido es mayor que el que conforma las muestras restantes")
                muestra_variacion = int(input("Cual es el tamaño de muestra: "))
                muestras.append(muestra_variacion)
            else:
                muestras.append(muestra_variacion)
            i += 1
        i = 0
        muestras_total.append(muestras)
        min += num_v
        j += 1
    print("\n\n---------------------------------------------------------\n")
    print("Tabla de Frecuencias en cada clase")
    i = 0
    print('Variaciones\t', end="")
    while i < num_variaciones:
        print("%.2f" % variaciones[i], '\t', end="")
        i += 1
    print("")

    clasif = []
    i = 0
    while i < len(clase):
        print(clase[i].nombre, "\t", end="")
        j = 0
        datos = []
        while j < num_variaciones:
            print(muestras_total[j][i], '\t', end="")
            dato = muestras_total[j][i] / clase[i].muestra
            datos.append(dato)
            j += 1
        clasif.append(datos)
        i += 1
        print()

    print("\n\n---------------------------------------------------------\n")
    print("Tabla de Distibuciones de cada clase")
    print(tabulate(clasif, variaciones, tablefmt='fancy_grid', stralign='center'))
    print("\n---------------------------------------------------------\n")

    opc = int(1)
    while opc >= 1:
        print("Probando el clasificador\n")

        prueba_clas = float(input("Introduce el patron desconocido a probar con el clasificador: "))
        if rasgo_max < prueba_clas or prueba_clas < rasgo_min:
            print("El patron desconocido no pertenece a las muestras aprendidas por el clasificador")
        else:
            d = []
            i = 0
            while i < len(variaciones):
                if prueba_clas == variaciones[i]:
                    print("Pertenece a la variacion", variaciones[i])
                    j = 0
                    while j < len(clase):
                        if clasif[j][i] != 0:
                            operacion = log(clase[j].muestra / muestra_total) + log(clasif[j][i])
                        else:
                            operacion = -100000000
                        print("Probabilidad de la clase",clase[j].nombre, "=", operacion)
                        d.append(operacion)
                        j += 1
                    i = len(variaciones)
                elif prueba_clas < variaciones[i]:
                    print("Pertenece a la variacion", variaciones[i-1])
                    j = 0
                    while j < len(clase):
                        if clasif[j][i-1] != 0:
                            operacion = log(clase[j].muestra / muestra_total) + log(clasif[j][i-1])
                        else:
                            operacion = -100000000
                        print("Probabilidad de la clase", clase[j].nombre, "=", operacion)
                        d.append(operacion)
                        j += 1
                    i = len(variaciones)
                else:
                    i += 1

            proba = d[0]
            aux = 0
            i = 1
            while i < len(clase):
                if proba < d[i]:
                    proba = d[i]
                    aux = i
                elif proba == d[i]:
                    proba = d[i]
                    aux = i
                i += 1

            print("Es probable que el dato desconocido sea", clase[aux].nombre, "con", proba, "%")

            opc = input("Desea probar otro patron? (Si = 1, No = 0)")


#------------------------------------------------------------------------------------------------------------------


def euclidiano():
    print("Opcion 2 - Euclidiano")
    num = int(input("Introduzca el numero de clases a manejar:"))
    clases = []
    i = 0
    while i < num:
        print("Cada patron debe contener 2 coordenadas - X y Y")
        num1 = int(input("Introduzca el numero de patrones que va a contener la clase %d: " % i))
        patrones = []
        cont = 0
        while cont < num1:
            print("Patron %d" % cont)
            x = input("Introduce x:")
            y = input("Introduce y:")
            coordenada = Coordenada(x, y)
            patrones.append(coordenada)
            cont += 1
        clases.append(patrones)
        i += 1

    opc = 1
    while opc == 1:
        i = 0
        x_grafica = []
        y_grafica = []
        figure()
        for clase in clases:
            cont = 0
            print('{', end="")
            for patron in clase:
                x_grafica.append(float(patron.obtener_x()))
                y_grafica.append(float(patron.obtener_y()))
                print('(', patron.obtener_x(), ",", patron.obtener_y(), " ),", end="")
                cont += 1
            print('}')
            i += 1

        x = (-30, 30)
        y = (0, 0)
        xlim([-10, 10])
        ylim([-10, 10])
        plot(x, y, 'black')
        plot(y, x, 'black')
        plot(x_grafica, y_grafica, marker='o', linestyle=' ', color='r')
        xlabel('x')
        ylabel('y')
        title('titulo')
        show()


        print("Ahora se probara el clasificador:")
        print("Introduce el patron desconocido")

        x_desconocido = float(input("Introduce a x:"))
        y_desconocido = float(input("Introduce a y:"))

        figure()

        x = (-30, 30)
        y = (0, 0)
        xlim([-10, 10])
        ylim([-10, 10])
        plot(x, y, 'black')
        plot(y, x, 'black')
        plot(x_grafica, y_grafica, marker='o', linestyle=' ', color='r')
        plot(x_desconocido, y_desconocido, marker='+', linestyle=' ', color='b')
        xlabel('x')
        ylabel('y')
        title('titulo')
        show()

        i = 0

        p_representante = []
        while i < len(clases):
            j = 0
            x = 0
            y = 0
            while j < len(clases[i]):
                x = x + float(clases[i][j].obtener_x())
                y = y + float(clases[i][j].obtener_y())
                j += 1
            operacion_x = (1/len(clases[i])) * x
            operacion_y = (1/len(clases[i])) * y
            operacion = Coordenada(operacion_x, operacion_y)
            print ("clase: ", i, ":", operacion_x, '/', operacion_y)
            p_representante.append(D(i,operacion))
            i += 1

        figure()

        x = (-30, 30)
        y = (0, 0)
        xlim([-10, 10])
        ylim([-10, 10])
        plot(x, y, 'black')
        plot(y, x, 'black')
        plot(x_grafica, y_grafica, marker='o', linestyle=' ', color='r')
        plot(x_desconocido, y_desconocido, marker='+', linestyle=' ', color='b')
        for representante in p_representante:
            plot(representante.num.obtener_x(),representante.num.obtener_y(),marker='*', linestyle=' ', color='g')
        xlabel('x')
        ylabel('y')
        title('titulo')
        show()

        d = []
        d1_x = float(0)
        d1_y = float(0)
        i = 0
        while i < len(p_representante):
            print("representante x",p_representante[i].num.obtener_x(),"y",p_representante[i].num.obtener_y())
            if p_representante[i].num.obtener_x() > x_desconocido:
                d1_x = p_representante[i].num.obtener_x() - x_desconocido
            elif p_representante[i].num.obtener_x() < x_desconocido:
                d1_x = x_desconocido - p_representante[i].num.obtener_x()
            else:
                d1_x = 0

            if p_representante[i].num.obtener_y() > y_desconocido:
                d1_y = p_representante[i].num.obtener_y() - y_desconocido
            elif p_representante[i].num.obtener_y() < y_desconocido:
                d1_y = y_desconocido - p_representante[i].num.obtener_y()
            else:
                d1_y = 0
            patron_d = Coordenada(d1_x,d1_y)
            d.append(D(p_representante[i].x,patron_d))
            i += 1

        d2 = []

        i = 0
        while i < len(d):
            if i == 0:
                d2_x = d[i].num.obtener_x()
                d2_y = d[i].num.obtener_y()
                d_final = Coordenada(d2_x,d2_y)
            else:
                if d_final.obtener_x() < d[i].num.obtener_x():
                    if d_final.obtener_y() < d[i].num.obtener_y():
                        d2_x = d[i].num.obtener_x() - d_final.obtener_x()
                        d2_y = d[i].num.obtener_y() - d_final.obtener_y()
                    elif d_final.obtener_y() > d[i].num.obtener_y():
                        d2_x = d[i].num.obtener_x() - d_final.obtener_x()
                        d2_y = d_final.obtener_y() -  d[i].num.obtener_y()
                    else:
                        d2_x = d[i].num.obtener_x() - d_final.obtener_x()
                        d2_y = 0

                elif d_final.obtener_x() > d[i].num.obtener_x():
                    if d_final.obtener_y() < d[i].num.obtener_y():
                        d2_x = d_final.obtener_x() -  d[i].num.obtener_x()
                        d2_y = d[i].num.obtener_y() - d_final.obtener_y()
                    elif d_final.obtener_y() > d[i].num.obtener_y():
                        d2_x = d_final.obtener_x() -  d[i].num.obtener_x()
                        d2_y = d_final.obtener_y() -  d[i].num.obtener_y()
                    else:
                        d2_x = d_final.obtener_x() -  d[i].num.obtener_x()
                        d2_y = 0
                else:
                    if d_final.obtener_y() < d[i].num.obtener_y():
                        d2_x = 0
                        d2_y = d[i].num.obtener_y() - d_final.obtener_y()
                    elif d_final.obtener_y() > d[i].num.obtener_y():
                        d2_x = 0
                        d2_y = d_final.obtener_y() -  d[i].num.obtener_y()
                    else:
                        d2_x = 0
                        d2_y = 0
            d2_d = math.sqrt((d2_x*d2_x)+(d2_y*d2_y))
            d2.append(D(d[i].x,d2_d))
            i += 1

        print("\n\n")
        d2_distancia_final = 0
        i = 0
        while i < len(d2):
            print("centro de la clase",d2[i].x, "con distancia respecto al patron desconocido de", d2[i].num)
            if i == 0:
                d2_distancia_final = d2[i]
            else:
                if d2[i].num < d2_distancia_final.num:
                    d2_distancia_final = d2[i]
            i += 1

        print("\n\nEL patron desconocido pertenece a la clase", d2_distancia_final.x, " con una distancia minima de", d2_distancia_final.num)

        figure()
        x = (-30, 30)
        y = (0, 0)
        xlim([-10, 10])
        ylim([-10, 10])
        plot(x, y, 'black')
        plot(y, x, 'black')
        plot(x_grafica, y_grafica, marker='o', linestyle=' ', color='r')
        plot(x_desconocido, y_desconocido, marker='+', linestyle=' ', color='b')
        for representante in p_representante:
            plot(representante.num.obtener_x(), representante.num.obtener_y(), marker='*', linestyle=' ', color='g')
        xlabel('x')
        ylabel('y')
        title('titulo')
        show()

        clases[d2_distancia_final.x].append(Coordenada(x_desconocido,y_desconocido))

        opc = int(input("Desea meter otro patron? (Si = 1, No = 0)"))


#------------------------------------------------------------------------------------------------------------------

def perceptron():
    print("\nPractica 3 Perceptron")
    num = int(input("\nIntroduzca el numero de clases a manejar:")) #Ingresa las clases 
    clases = []
    i = 0
    while i < num:
        print("Cada patron debe contener 2 coordenadas - X y Y") ##Llena las clases
        num1 = int(input("Introduzca el numero de patrones que va a contener la clase %d: " % i))
        patrones = []
        cont = 0
        while cont < num1:
            print("Patron %d" % cont)
            x = int(input("Introduce x:"))
            y = int(input("Introduce y:"))
            coordenada = Coordenada(x, y)
            patrones.append(coordenada)
            cont += 1
        clases.append(patrones)
        i += 1

    alpha = float(input("\nIngrese la razon de aprendizaje (alpha) :")) #Razon de aprendizaje

    #Aumentar los patrones
    print("\nConvirtiendo los patrones de las clases en Vectores Patrón Aumentados")
    v_aumentado = []
    for clase in clases:
        p_aumentado = []
        for patron in clase:
            patron_x = patron.obtener_x()
            patron_y = patron.obtener_y()
            p_aumentado.append(V_ampliado(patron_x,patron_y,1,0))
        v_aumentado.append(p_aumentado)


    num_clase = 0
    for v in v_aumentado: #Mostrar patron aumentado
        print("\nclase",num_clase)
        for vector in v: 
            print("(",vector.obtener_x(),",",vector.obtener_y(),",",vector.obtener_b(),")")
        num_clase += 1

    #Inicializacion de los pesos
    print("\nInicializando w1, w2 y w3")
    w1 = w2 = w3 =0
    w = clase_w(1,w1,w2,w3)
    print("w",w.num,"(",w.w1,",",w.w2,",",w.w3,")")

    num_patron = 1
    acertados = 0

    vec_acertados = []
    for v in v_aumentado:
        for vector in v: 
            vec_acertados.append(vector.flag)

    num_correcto = 0
    num_total_acertados = len(vec_acertados)
    while acertados == 0:
        num_clase = 0
        for v in v_aumentado:
            for vector in v:
                print("\nIteracion num:",num_patron)
                print("w",w.num,"(",w.w1,",",w.w2,",",w.w3,")")

                print("\nX = (",vector.obtener_x(),",",vector.obtener_y(),",",vector.obtener_b(),")")

                resultado = (w.w1 * vector.obtener_x()) + (w.w2 * vector.obtener_y()) + (w.w3 * vector.obtener_b())
                print("w",w.num,"* X = (",w.w1,")(",vector.obtener_x(),")+(",w.w2,")(",vector.obtener_y(),")+(",w.w3,")(",vector.obtener_b(),") = ",resultado)

                if num_clase == 0:
                    if resultado <= 0:
                        print("Error")
                        print("\n Ajuste:")

                        print("w",w.num +1 ," = (",w.w1,",",w.w2,",",w.w3,") + (1)(",vector.obtener_x(),vector.obtener_y(),vector.obtener_b(),")")

                        w.num += 1
                        w.w1 = w.w1 + (1*vector.obtener_x())
                        w.w2 = w.w2 + (1*vector.obtener_y())
                        w.w3 = w.w3 + (1*vector.obtener_b())

                        vector.flag = 0

                        print("w",w.num,"= (",w.w1,",",w.w2,",",w.w3,")")
                    elif resultado >0:
                        print("Acierto")
                        vector.flag = 1
                elif num_clase == 1:
                    if resultado <= 0:
                        print("Acierto")
                        vector.flag = 1
                    elif resultado >0:
                        print("Error")
                        print("\n Ajuste:")

                        print("w",w.num +1 ," = (",w.w1,",",w.w2,",",w.w3,") - (1)(",vector.obtener_x(),vector.obtener_y(),vector.obtener_b(),")")

                        w.num += 1
                        w.w1 = w.w1 - (1*vector.obtener_x())
                        w.w2 = w.w2 - (1*vector.obtener_y())
                        w.w3 = w.w3 - (1*vector.obtener_b())

                        vector.flag = 0

                        print("w",w.num,"= (",w.w1,",",w.w2,",",w.w3,")")

                num_patron += 1
            num_clase += 1
            sleep(1)

        cont_aciertos = 0    
        for v in v_aumentado:
            for vector in v:
                if vector.flag == 0:
                    cont_aciertos += 1
        
        if cont_aciertos != 0:
            acertados = 0
        else:
            acertados = 1
        

    print("w final:")
    print("w = (",w.w1,",",w.w2,",",w.w3,")")

    print("w = %+d" % w.w1,"x1 %+d" % w.w2,"x2 %+d" % w.w3, sep='')

    opc = 1
    while opc >= 1:
        print("\n\nAhora se probara el clasificador:")
        print("Introduce el patron desconocido")

        x_desconocido = float(input("Introduce a x:"))
        y_desconocido = float(input("Introduce a y:"))

        print("X = ","(",w.w1,")(",x_desconocido,") + (",w.w2,")(",y_desconocido,") + ",w.w3,sep='')

        res_patron_desconocido = (w.w1*x_desconocido)+(w.w2*y_desconocido)+(w.w3)

        if res_patron_desconocido >= 1:
            print("Pertenece a la clase 0")
            v_aumentado[0].append(V_ampliado(x_desconocido,y_desconocido,1,1))
        else:
            print("Pertenece a la clase 1")
            v_aumentado[1].append(V_ampliado(x_desconocido,y_desconocido,1,1))

        opc = int(input("Desea introducir otro patron? (Si = 1, No = 0)"))


#---------------------------------------------------------

class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# regresa el valor de x
    def obtener_x(self):
        return self.x

# regresa el valor de y
    def obtener_y(self):
        return self.y

#---------------------------------------------------------

class V_ampliado:
    def __init__(self, x, y, b, flag):
        self.x = x
        self.y = y
        self.b = b
        self.flag = flag

# regresa el valor de x
    def obtener_x(self):
        return self.x

# regresa el valor de y
    def obtener_y(self):
        return self.y

# regresa el valor de b
    def obtener_b(self):
        return self.b

# regresa el valor de b
    def obtener_flag(self):
        return self.flag
#---------------------------------------------------------

class clase_w:
    def __init__(self,num, w1, w2, w3):
        self.num = num
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        

# regresa el valor de num de w
    def obtener_num(self):
        return self.num

# regresa el valor de w1
    def obtener_w1(self):
        return self.w1

# regresa el valor de w2
    def obtener_w2(self):
        return self.w2

# regresa el valor de w3
    def obtener_w3(self):
        return self.w3

#---------------------------------------------------------
class D:
    def __init__(self, x, num):
        self.x = x
        self.num = num

# regresa el valor de x
    def obtener_x(self):
        return self.x

# regresa el valor de num
    def obtener_num(self):
        return self.num
#---------------------------------------------------------

class Patron:
    def __init__(self, nombre, muestra):
        self.nombre = nombre
        self.muestra = muestra

# regresa el nombre
    def obtener_nombre(self):
        return self.nombre

# regresa el valor de la muestra
    def obtener_muestra(self):
        return self.muestra
#---------------------------------------------------------

print("---------------------------------------------------------")
print("Programa que realiza la clasificacion de Patrones a partir")
print("de operaciones y clasificadores de enfoque:\n")
print("*Estadisticos-Probabilisticos\t*Basados en Metricas\t*Algoritmos Lineales")
print("---------------------------------------------------------\n\n")

print("En esta caso toca el turno del Perceptron")
print("Perceptron")
print("\n\n---------------------------------------------------------\n")
"""opcion = input("Elija una opcion: ")
opcion = '3'
if opcion == '1':
    bayesiano_simple()
elif opcion == '2':
    euclidiano()
elif opcion == '3':"""
perceptron()