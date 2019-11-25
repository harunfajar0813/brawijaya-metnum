import numpy as np
import matplotlib.pyplot as plt
import random

# f = open("C:/Users/HARUN/Documents/GitLab/brawijaya-metnum/tugas3_final/titik_x_y.txt", 'r')
# baris1 = f.read().split(',')
# x = []
# y = []
# jumlah = 20
# for i in range(jumlah):
#     if (i <= ((jumlah / 2) - 1)):
#         x.append(int(baris1[i]))
#     else:
#         y.append(int(baris1[i]))
n = 1000
x = np.random.randint(10, size=n)
y = np.random.randint(10, size=n)
for i in range(n):
    random_temp = np.random.randint(10, size=1)
    if (x[i] == y[i]):
        y[i] = random_temp[0]


def lagrange(x, y, x_int):
    n = x.size
    y_int = 0

    for i in range(0, n):
        p = y[i]
        j = 1
        for j in range(0, n):
            if (i != j):
                p = p * (x_int - x[j]) / (x[j] - x[i])
            elif (i < j):
                continue
        y_int = y_int + p
    return y_int

fx = np.arange(0,len(x),0.01)
A = lagrange(np.array(x), np.array(y), fx)
print(A)

plt.plot(x,y,'r-')
plt.show()
plt.title("Langrage")
plt.axhline(y=0, color='b')

print(np.random.randint(1000, size=1000))