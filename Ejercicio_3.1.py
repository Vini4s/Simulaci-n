from random import random
from math import exp,sqrt

N=100000
n2=[]
for i in range(N):
    u=0
    n=0
    while u<=1:
        n=n+1
        u=u+random()
    n2.append(n)
Media_muestral=sum(n2)/N
print("La esperanza de N es",Media_muestral)

Suma=sum([i-Media_muestral for i in n2])**2
ds=sqrt(1/(N-1)*Suma)
print("Intervalo de confianza al 95% es [",Media_muestral-1.65*(ds/sqrt(N)),
" , ",Media_muestral-1.65*(ds/sqrt(N))," ]")

