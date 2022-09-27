from random import random
import matplotlib.pyplot as plt
def gen(lx):
  x=random()
  lx.append(round(x,1))
  if x<0.1:
    return 1
  elif x<0.3 and x>0.1:
     return 2
  elif x<0.7 and x>0.3:
     return 5
  else:
     return 8

N=100
ly=[]
l=[]
lx=[]
for i in range (N):
  x=random()s
  ly.append(gen(lx))
  l.append(i+1)
plt.plot(l,ly)
plt.show()
plt.plot(l,lx)
plt.show()