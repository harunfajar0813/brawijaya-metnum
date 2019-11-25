import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0,4.0,0.05)
y = x**3 - 6*(x**2) + 11*x - 6.1

Er = 10
Es = 0.001

Fx = lambda x: x**3 - 6*(x**2) + 11*x - 6.1
FX = lambda x: 3*(x**2)- 12*x + 11

Xnow = 3.5
Xnext = 100
n = 1
print("Iterasi\t Xn \t\t Xn+1 \t\t Fx(Xn) \t F'x(Xn) \t Er")
while(Er > Es and n < 6):
    Xnext = Xnow - (Fx(Xnow) / FX(Xnow))
    print("%d \t %f \t %f \t %f \t %f \t %f \t"%(n,Xnow,Xnext,Fx(Xnow),FX(Xnow), Er))
    Er = (abs(Xnow - Xnext)/Xnext) * 100
    plt.plot(Xnow,Fx(Xnow),"o",color = 'green')
    Xnow = Xnext
    n = n + 1

plt.plot(x,y,'-')
plt.axhline(y=0,color='r')
plt.grid(True)
plt.show()