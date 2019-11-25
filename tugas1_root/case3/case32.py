import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: x**3 - 6*(x ** 2) + 11*(x ** 1) - 6.1
gx = lambda x: (-x**3 + 6*(x ** 2) + 6.1)/11
x = np.arange(0.0, 4.0, 0.01)
y = x**3 - 6*(x**2) + 11*x - 6.1

plt.plot(x, y, '-')
plt.xlabel('X');
plt.ylabel('Y');
plt.axhline(y=0, color='r')
plt.grid(True)

a = 3.5

i = 0
n = 0
Er = 100

print("Iterasi\t  X0\t   XR+1\t    Er\t")
while abs(Er) > 0.001:
    xn = gx(a)
    Er = ((xn - a) / xn) * 100
    plt.plot(a, fx(a), markersize=5, marker='o', color='green')
    print("%d\t%f  %f  %f" % (n, a, xn, abs(Er)))
    n += 1
    a = xn

print("Akar nya ialah %f" % (a))
