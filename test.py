import matplotlib.pyplot as plt
import numpy as np

# taking two inputs at a time 
#a, b = input("Enter a two value: ").split() 
x = list(map(int, input("Enter a multiple value: ").split()))
y = list(map(int, input("Enter a multiple value: ").split()))

a = [1,2]
b = [5,6]
aux = []
aux.append(x)
aux.append(y)
clases = []
clases.append(aux)
aux = []
aux.append(a)
aux.append(b)
clases.append(aux)

print("Number of boys: ", clases) 
print(clases[0][1][1])



#while c < n:
#plt.plot(t,y)
#plt.plot(r,q)
#   c = c+1

#plt.show()

