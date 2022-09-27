from random import random
from math import exp
from scipy.stats import poisson
def poison(lam):
  u=random()
  p0=exp(-lam)
  pk=p0
  sk=p0
  k=0
  while u>sk:
    pk=pk*lam/(k+1)
    sk=sk+pk
    k=k+1
  return k
lam=5
for i in range(10):
  print(poison(lam),' ',end='')