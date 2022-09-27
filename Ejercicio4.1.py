from random import random
from math import pi,exp,sqrt,sin
from re import X
from Calculo_de_integrales import Int_0_1,Int_a_b,Int_0_inf

def fx(x):
    return exp(-(x**2))
def gx(x):
    return sqrt(1+x**3)
def hx(x):
    return sin(x)/x
#a)
print("La aproximación de la integral a) es ",Int_0_1(gx))
#b)
print("La aproximación de la integral b) es ",Int_a_b(fx,3,5))
#c)
print("La aproximación de la integral c) es ",Int_a_b(hx,0.5,1))
#d)
print("La aproximación de la integral d) es ",Int_0_inf(fx))
#e)
print("La aproximación de la integral e) es ",2*Int_0_inf(fx))
#f)
print("La aproximación de la integral f) es ",Int_0_inf(fx)-Int_a_b(fx,0,2)),