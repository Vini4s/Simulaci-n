from random import random
def binomial(n,p):
  u=random()
  p0=(1-p)**n
  pk=p0
  sk=p0
  k=0
  while u>sk:
    pk=pk*(n-k)*p/((k+1)*(1-p))
    sk=sk+pk
    k=k+1
  return k

n=10
p=0.4
for i in range(100):
  print(binomial(n,p),' ',end='')