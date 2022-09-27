from random import random
from math import log
import matplotlib.pyplot as plt

#Se programa la función de densidad f(x)
def fx(u):
    if u>1 and u<2:
        return log(u)/((2*log(2))-1)
    else:
        return 0
#Se programa la función de densidad f(y)
def fy(u):
    if u>1 and u<2:
        return 1
    else:
        return 0
#Se programa la generación de variable aleatoria y
def genY():
    u=random()
    return u+1

#Se programa el método de aceptación y rechazo que genera variables aleatorias de x
def genX(c):
    zk=genY()
    u=random()
    while u>=fx(zk)/(c*fy(zk)):
        zk=genY()
        u=random()
    return zk
c=1.8
n=100000
l=[]
#Revisar la distribución de la variable x
for i in range(n):
    #print(genX(c)," ",end="")
    x=genX(c)
    l.append(x)
b=[]
x1=1
x2=2
x=1
while x<=x2:
    b.append(x)
    x=x+(x2-x1)/50
lx=[]

for i in b:
    lx.append(log(i)/((2*log(2))-1))

plt.hist(l,bins=b,density=1,color="grey",edgecolor="black")
plt.plot(b,lx,color="red",lw=2)
plt.show()

