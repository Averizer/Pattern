import matplotlib.pyplot as plt
import numpy as np

# taking two inputs at a time 
a, b = input("Enter a two value: ").split() 
print("Number of boys: ", a) 
print("Number of girls: ", b) 


t =[1,3,2]
y =[2,4,6]

r =[3,3,2]
q =[2,3,5]
c=0
c2=0

x , y = input("Ingresa la caracteristica X= ").split()
x= int(x)
y=int(y)
print(x)
print(y)
#while c < n:
plt.plot(t,y)
plt.plot(r,q)

 #   c = c+1

plt.show()

