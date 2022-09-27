from random import random
from math import exp

n=10000
N=0
for i in range(n):
    u=[]
    for j in range(10):
        u.append(random())
    N=N+max(u)

print("La esperanza de N es", N/n)