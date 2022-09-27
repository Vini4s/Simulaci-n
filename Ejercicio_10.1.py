from random import random
from math import sqrt,log

N=10000
Suma=0
for i in range(N):
    suma=0
    for j in range(5):
        x=random()
        suma=suma+x
    Suma=Suma+suma
print("La espernza es ",Suma/N)