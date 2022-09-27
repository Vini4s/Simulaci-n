from ast import Return
from random import random

def juego(a,b):
    while a>0 and b>0:
        if random()<0.5 :
            a=a-1
            b=b+1
        else:
            b=b-1
            a=a+1
    return[a,b]

#Cuantos juegos gana cada jugador y su probabilidad
n=100000
a=12
b=12
jb=0
ja=0
for i in range(n):
    if juego(a,b)[0]==0:
        jb=jb+1
    else:
        ja=ja+1
print("Juegos ganados de a ",ja)
print("Juegos ganados de b ",jb)
print("Probabilidad de a ",ja/n)
print("Probabilidad de b ",jb/n)

