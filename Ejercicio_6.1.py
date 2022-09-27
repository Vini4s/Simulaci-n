from random import random
from math import sqrt,log
def fx():
    x=random()
    if x<0.1:
        return 1
    elif x<0.2:
        return 2
    elif x<0.5:
        return 3
    else:
        return 4
N=100000
suma=0
for i in range(N):
    suma=suma+(1/(1+fx()**2))
print("El valor esperado es ",suma/N)