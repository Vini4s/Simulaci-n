from random import random
from math import sqrt,log

N=100000
suma=0
for i in range(N):
    x=1+int(log(1-random())/log(1/3))
    suma=suma+x**2
print("La esperanza es ",suma/N)