from random import random
from math import sqrt,log

N=10000
suma=0
n=0
for i in range(N):
    x=2**(random())
    suma=suma+(sqrt(1+x**2))
    if x<1.8 and x>1.3:
        n=n+1
print("La esperanza des",suma/N)
print("La probabilidad de que 1.3<X<1.8 es ",n/N)