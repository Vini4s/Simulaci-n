from random import random
from math import sqrt, pi

n=0
N=100000000

for i in range(N):
    if (random())**2+(random())**2+(random())**2<1:
        n=n+1
print("Aproximación por simulación",(8*n/N))
print("Vallor exacto",4/3*pi)

