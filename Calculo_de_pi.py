from random import random
from matplotlib import pyplot
from math import pi
n=0
N=10000000
lx=[]
ly=[]
l=[]
for i in range(N):
    x=random()
    y=random()
    if x**2+y**2<1:
        n=n+1
        if i%100000==0 and i>0:
            lx.append(i)
            ly.append(4*n/(i+1))
            l.append(pi)

pyplot.plot(lx,ly,color="black",label="Simulación")
pyplot.plot(lx,l,color="orange",label="Valor exacto")
pyplot.legend()
pyplot.show()
#pyplot.savefig("Simulación de Pi.png",dpi=12000)
