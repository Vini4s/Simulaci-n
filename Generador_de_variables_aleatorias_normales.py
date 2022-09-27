from random import random
from math import log,sqrt,pi,cos
import matplotlib.pyplot as plt
l=[]
n=1000000
for i in range(n):
    u1=random()
    u2=random()
    x=sqrt(-2*log(u2))*cos(2*pi*u1)
    l.append(x)
plt.hist(l,density=1,bins=30,color="gray",edgecolor="black")
plt.show()
