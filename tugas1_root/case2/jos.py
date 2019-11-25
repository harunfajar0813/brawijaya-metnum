import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-3,3,0.01)
y = x**4 - 2*(x**2) + x - 3
Fx = lambda x : x**4 - 2*(x**2) + x - 3
# x0=float(input("Masukkan x0: "))
# x1=float(input("Masukkan x1: "))
Es = 0.0001
Er = 100.0
Xnow = 2.75
Xprev = 1
n = 1
print("Iterasi\t Xn-1\t\t Xn \t\t Xn+1 \t\t F(Xn-1) \t F(Xn) \t\t F(Xn+1) \t Er")
while(Er > Es):
    Xnext = Xnow -(Fx(Xnow)*(Xnow - Xprev)/(Fx(Xnow)-Fx(Xprev)))
    Er = abs((Xnow - Xprev)/Xnext)
    print("%d \t %f \t %f \t %f \t %f \t %f \t %f \t %f"%
          (n,Xprev,Xnow,Xnext,Fx(Xprev),Fx(Xnow),Fx(Xnext),Er))
    plt.plot(Xnow,Fx(Xnow),'.')
    Xprev = Xnow
    Xnow = Xnext
    n += 1

plt.title("Metode Secant")
plt.plot(x,y,'-')
plt.axhline(y=0,color='r')
plt.show()