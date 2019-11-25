import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.linspace(0,4)
plt.plot(x, (x**3)-(6*x**2)+(11*x)-6.1, '-r', label='y=x^3-6x^2+11x-6.1')
plt.axhline(y=0,color='g')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()