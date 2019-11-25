import numpy as np
from scipy.linalg import lu
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5])
n = len(x)
x_mean = np.mean(x)
x0 = sum(x)
x1 = sum(x**2)
x2 = sum(x**3)
x3 = sum(x**4)
y = np.array([2.1,7.7,13.6,27.2,40.9,61.1])
y0 = sum(y)
y_mean = np.mean(y)
#
# x_kali_y = sum(x*y)
# x2_kali_y = sum((x**2)*y)
#
from numpy import array
from scipy.linalg import lu

# a = array([[2.,4.,4.,4.],[1.,2.,3.,3.],[1.,2.,2.,2.],[1.,4.,3.,4.]])
a = array([[n,x0,x1],[x0,x1,x2],[x1,x2,x3]])
print(a)

pl, u = lu(a)
print(u)