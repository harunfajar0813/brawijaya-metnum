import random
import matplotlib.pyplot as pt
import statistics as ss
import numpy as np

def generate_data():
	x = np.array([])
	y = np.array([])
	for i in range(1000):
		x.append(random.randrange(10))
		y.append(random.randrange(10))
	return [x,y]

def final():
	data = generate_data()
	nilai_x = data[0]
	nilai_y = data[1]
	return [nilai_x,nilai_y]

print(final()[0])
# print(final()[1])
pt.scatter(final()[0], final()[1])
pt.show()

