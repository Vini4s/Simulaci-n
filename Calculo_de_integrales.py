from random import random
from math import pi,exp

#Integrales de 0 a 1
def Int_0_1(fx):
    n=100000
    suma=0
    for i in range(n):
        suma=suma+fx(random())
    return suma/n

#Integrales de a-b
def Int_a_b(fx,a,b):
    n=100000
    suma=0
    for i in range(n):
        suma=suma+fx(random()*(b-a)+a)*(b-a)
    return suma/n

#Integrales de 0 a infinito
def Int_0_inf(fx):
     n=100000
     suma=0
     for i in range(n):
        r=random()
        suma=suma+(fx((1/r)-1)*(1/r**2))
     return suma/n
