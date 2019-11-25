import numpy as np
import matplotlib.pyplot as plt
fx = lambda x : x**3-6*(x**2)+11*x-6.1
x0=float(input("Masukkan x0: "))
x1=float(input("Masukkan x1: "))
i=0
Er=100
if(x0!=0):
  print("Iterasi\t\t x0\t\t XnEr")
  while abs(Er)>0.1:
    xn = x1 -((fx(x1)*(x1-x0))/(fx(x1)-fx(x0)))
    Er = ((xn-x0)/xn)*100
    print ("%d\t    %f\t    %f\t    %f\t"
           "%f\t    %f"%(i,x0,x1,xn,fx(xn),abs(Er)))
    x0 = x1
    x1 = xn
    i+=1
  print("Root : %f" % (xn))
else:
  print("Penentuan xn salah")