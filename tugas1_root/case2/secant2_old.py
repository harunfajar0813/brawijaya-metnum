import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-3,3,0.01)
y = (x**4)-(2*(x**2))+(11*x)-6.1
fx = lambda x : (x**4)-(2*(x**2))+(11*x)-6.1
# x0=float(input("Masukkan x0: "))
# x1=float(input("Masukkan x1: "))
Es = 0.0001
Er = 100.0
x1 = 2.75
x0 = 1
i = 0

if(x0!=0):
  print("Iterasi\t Xn-1\t\t Xn \t\t Xn+1 \t\t F(Xn-1) \t F(Xn) \t\t F(Xn+1) \t Er")
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