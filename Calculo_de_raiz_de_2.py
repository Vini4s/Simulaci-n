from random import random
from matplotlib import pyplot
from math import sqrt

n=0
N=10000000
#lx=[]
#ly=[]
#l=[]
for i in range(N):
    x=(random()+1)**2
    if x<2:
        n=n+1
        #if i%100000==0 and i>0:
            #lx.append(i)
            #ly.append(n/i+1)
            #l.append(sqrt(2))
print("Aproximación de la simulación",n/N+1)
print("Vallor exacto",sqrt(2))
#pyplot.plot(lx,ly,color="black",label="Simulación")
#pyplot.plot(lx,l,color="orange",label="raiz de dos")
#pyplot.legend()
#pyplot.show()


