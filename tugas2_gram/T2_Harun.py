import numpy as np

a_utama1 = np.array([[1.0,1.0,0.0], [1.0,0.0,1.0], [0.0,1.0,1.0]])
a_utama2 = np.array([[1.0,1.0,0.0], [1.0,0.0,1.0], [0.0,1.0,1.0]])
b_utama = np.array([0.1, 0.9, 2.0])

def hitung_proyeksi(a_berapa,e_berapa):
    return ((np.dot(a_berapa,e_berapa) * e_berapa) * (-1))

def hitung_e(u_berapa):
    return (u_berapa / np.linalg.norm(u_berapa))

def backward(R,b): # Backward Substitution
    n = len(R)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            b[i] = b[i] - R[i, j] * x[j]
        x[i] = b[i] / R[i, i]
    return x

def gram_schmidt_q(matriks):
    u_total = []
    e_total = []
    pecah_matriks = matriks.transpose()
    for jumlah_perulang_gs in range(len(matriks[0])):
        u_total.append(pecah_matriks[jumlah_perulang_gs])
        for banyak_proyeksi in range(jumlah_perulang_gs):
            u_total[jumlah_perulang_gs] += hitung_proyeksi(pecah_matriks[jumlah_perulang_gs], e_total[banyak_proyeksi])
        e_total.append(hitung_e(u_total[jumlah_perulang_gs]))

    Q = np.array(e_total).transpose()
    QT = Q.transpose()
    return [u_total,e_total,Q,QT]

def gram_schmidt_r(matriks,e_total):
    pecah_matriks = matriks.transpose()
    R = np.zeros((len(matriks[0]), len(matriks[0])))
    for i in range(len(matriks[0])):
        for j in range(len(matriks)):
            if (j > i):
                continue
            R[j][i] = np.dot(pecah_matriks[i], e_total[j])

    return [R]

def hasil():
    nilai_q = gram_schmidt_q(a_utama1)
    u_Total = nilai_q[0]
    e_Total = nilai_q[1]
    q = nilai_q[2]
    qt = nilai_q[3]
    nilai_r = gram_schmidt_r(a_utama2,nilai_q[1])
    r = nilai_r[0]
    nilai_backward = backward(nilai_r[0],b_utama)
    return [a_utama2,b_utama,u_Total,e_Total,q,qt,r,nilai_backward]

hasil_akhir = hasil()
print('Hasil Akhir')
print()
print('a utama = ',a_utama2)
print()
print('a1 = ',a_utama2.transpose()[0])
print('a2 = ',a_utama2.transpose()[1])
print('a3 = ',a_utama2.transpose()[2])
print()
print('b utama = ',hasil_akhir[1])
print()
print('u total = ',hasil_akhir[2])
print()
print('e total = ',hasil_akhir[3])
print()
print('Q = ',hasil_akhir[4])
print()
print('Q Transpose = ',hasil_akhir[5])
print()
print('R Transpose = ',hasil_akhir[6])
print()
print('Backward = ',hasil_akhir[6])