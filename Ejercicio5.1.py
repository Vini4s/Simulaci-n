from random import random
from math import sqrt,log

N=1000000
suma=[]
for i in range(N):
    x=1+int((log(1-random()))/(log(1-0.2)))
    suma.append(sqrt(1+x))
Media_muestral=sum(suma)/N
print("La esperanza de N es",Media_muestral)

Suma=sum([i-Media_muestral for i in suma])**2
ds=sqrt(1/(N-1)*Suma)
print("Intervalo de confianza al 95% es [",Media_muestral-1.65*(ds/sqrt(N)),
" , ",Media_muestral-1.65*(ds/sqrt(N))," ]")
