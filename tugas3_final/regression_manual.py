# Linear Regression
import numpy as np
import random
import matplotlib.pyplot as plt

def olah_data(jumlah_data,digit_angka):
    X = []
    # X = titik.readline()
    Y = []
    # Y = titik.readline()
    for i in range(jumlah_data):
        X.append(random.randrange(digit_angka))
        Y.append(random.randrange(digit_angka))
    # f = open("C:/Users/HARUN/Documents/GitLab/brawijaya-metnum/tugas3_final/titik_x_y.txt", 'r')
    # baris1 = f.read().split(',')
    # X = []
    # Y = []
    # jumlah = 20
    # for i in range(jumlah):
    #     if (i <= ((jumlah / 2) - 1)):
    #         X.append(int(baris1[i]))
    #     else:
    #         Y.append(int(baris1[i]))
    return [X,Y]

def rumus1(X,Y,mean_x,mean_y,index):
    return (X[index] - mean_x) * (Y[index] - mean_y)

def rumus2(X,mean_x,index):
    return (X[index] - mean_x) ** 2

def menggambar_pola(x_garis,y_garis,X_titik,Y_titik):
    plt.plot(x_garis, y_garis, color='#58b970')
    plt.scatter(X_titik, Y_titik, c='#ef5423')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def hasil():
    data = olah_data(10,1000)

    mean_x = np.mean(data[0])
    mean_y = np.mean(data[1])

    panjang_data = len(data[0])

    hasil1 = 0
    hasil2 = 0

    for i in range(panjang_data):
        hasil1 += rumus1(data[0],data[1],mean_x,mean_y,i)
        hasil2 += rumus2(data[0],mean_x,i)

    b1 = hasil1 / hasil2
    b0 = mean_y - (b1 * mean_x)

    max_x = np.max(data[0]) + 100
    min_x = np.min(data[0]) - 100

    x = np.linspace(min_x, max_x, 1000)
    y = b0 + b1 * x

    return [b1,b0,x,y,data]

# panggil metode utama
hasil_akhir = hasil()
print('b1 =',hasil_akhir[0])
print('b2 =',hasil_akhir[1])
print('x =',hasil_akhir[2])
print('y =',hasil_akhir[3])
menggambar_pola(hasil_akhir[2], hasil_akhir[3], hasil_akhir[4][0], hasil_akhir[4][1])
