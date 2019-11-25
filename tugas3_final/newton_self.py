# newton
import numpy as np
import matplotlib.pyplot as plt

# n = 200
# # a = np.array(random.sample(range(1000), n))
# a = np.array([20, 33, 97, 14, 95, 21, 36, 50, 73, 39])
# # b = np.array(random.sample(range(1000), n))
# b = np.array([20, 33, 97, 14, 95, 21, 36, 50, 73, 39])
# for i in range(len(a)):
#     random_temp = random.sample(range(100), 1)
#     if(a[i] == b[i]):
#         b[i] = random_temp[0]
f = open("C:/Users/HARUN/Documents/GitLab/brawijaya-metnum/tugas3_final/titik_x_y.txt", 'r')
baris1 = f.read().split(',')
a = []
b = []
jumlah = 20
for i in range(jumlah):
    if (i <= ((jumlah / 2) - 1)):
        a.append(int(baris1[i]))
    else:
        b.append(int(baris1[i]))

def newtonFFS(x, y):
    """ membuat Newton pyramid and hasil ffs """
    n = np.shape(y)[0]
    pyramid = np.zeros([n, n])
    pyramid[::,0] = y # membuat kolom pertama y
    for j in range(1,n):
        for i in range(n-j):
            pyramid[i][j] = (pyramid[i+1][j-1] - pyramid[i][j-1]) / (x[i+j] - x[i])
    return pyramid[0] # return baris

coeff_vector = newtonFFS(a, b)
print("Hasil koefesien : ")
print(coeff_vector)
print(" ")

final_pol = np.polynomial.Polynomial([0.])
n = coeff_vector.shape[0] # memangil koefisien
for i in range(n):
    p = np.polynomial.Polynomial([1.])
    for j in range(i):
        p_temp = np.polynomial.Polynomial([-a[j], 1.]) # (x - x_j)
        p = np.polymul(p, p_temp)
    p *= coeff_vector[i]
    final_pol = np.polyadd(final_pol, p)

p = np.flip(final_pol[0].coef, axis=0)
print(p)

x_axis = np.linspace(0, 10, num=5000)
y_axis = np.polyval(p, x_axis)
plt.plot(x_axis, y_axis)
# plt.scatter(a,b)
plt.show()
