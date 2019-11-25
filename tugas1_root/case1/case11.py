import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = np.linspace(0.9,1.2)
plt.plot(x, x**10-1, '-r', label='y=x^10-1')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()