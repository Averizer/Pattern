#DECLARANDO LOS CONJUNTOS DE PRUEBAS
conjunto_x = [[0,1,0,0,1],[1,1,0,1,1],[1,1,1,1,0]]
conjunto_y =[[1,0,0],[0,1,0],[0,0,1]]

#FASE DE APRENDIZAJE
matriz_aprendizaje = []
#inicializar matriz_aprendizaje
print("Entrenando la matríz...")

for a in range(3):
    aux = []
    for b in range(5):
        aux.append(0)
    matriz_aprendizaje.append(aux)

for clase in range(3):
    for y_interno in range(3):
        if(conjunto_y[clase][y_interno] == 1):
            aux_construccion = []
            for x_actual in range(5):
                #print("Actual: "+str(x_actual))
                if (conjunto_x[clase][x_actual] == 1):
                    #clsprint("Agregado de la clase {} valor de x {}".format(clase, x_actual))
                    matriz_aprendizaje[clase][x_actual] = matriz_aprendizaje[clase][x_actual] + 1
                else:
                    matriz_aprendizaje[clase][x_actual] = matriz_aprendizaje[clase][x_actual] - 1

print("La matriz se ha entrenado correcatemente, resultado recuperado: ")
for i in matriz_aprendizaje:
    print(i)

    
#FASE DE PRUEBA 
patron_prueba = [1,1,1,1,0]
valores = []
for clase in range(3):
    aux_valor_total_clase = 0
    for valor_actual in range(5):
        if(patron_prueba[valor_actual] == 1):
            aux_valor_total_clase += matriz_aprendizaje[clase][valor_actual] 
        else:
            aux_valor_total_clase += 0
    valores.append(aux_valor_total_clase)

mayor = max(valores)
print("\n\nPRUEBA 1")
print("Los valores son: ")
print(valores)
print("El patron pertenece a la clase {}".format(valores.index(mayor)))     


patron_prueba = [1,1,0,1,1]
valores = []
for clase in range(3):
    aux_valor_total_clase = 0
    for valor_actual in range(5):
        if(patron_prueba[valor_actual] == 1):
            aux_valor_total_clase += matriz_aprendizaje[clase][valor_actual] 
        else:
            aux_valor_total_clase += 0
    valores.append(aux_valor_total_clase)

mayor = max(valores)
print("\n\nPRUEBA 2")
print("Los valores son: ")
print(valores)
print("El patron pertenece a la clase {}".format(valores.index(mayor)))     
