import numpy as np

a_utama = np.array([[1.0,-1.0,4.0],[1.0,4.0,-2.0],[1.0,4.0,2.0],[1.0,-1.0,0.0]])
# a_utama = np.array([[1.0,1.0,0.0],
#                     [1.0,0.0,1.0],
#                     [0.0,1.0,1.0]])

pecah_matrix = a_utama.transpose()
# print(pecah_matrix[1])
u_total = []
e_total = []
#
def hitung_proyeksi(a_berapa,e_berapa):
    return ((np.dot(a_berapa,e_berapa) * e_berapa))
#
def hitung_e(u_berapa):
    return (u_berapa / np.linalg.norm(u_berapa))

# alur pemahaman JANGAN DIHAPUS
# u0 dan e0
print()
print('untuk a0 = ', pecah_matrix[0])
u_total.append(pecah_matrix[0])
print('u1 = ', u_total[0])
e_total.append(hitung_e(u_total[0]))
print('e1 = ',e_total[0])

# u1 dan e1
print()
print('untuk a2 = ', pecah_matrix[1])
u_total.append(pecah_matrix[1] - hitung_proyeksi(pecah_matrix[1],e_total[0]))
print('u2 = ', u_total[1])
e_total.append(hitung_e(u_total[1]))
print('e2 = ', e_total[1])

# u2 dan e2
print()
print('untuk a3 = ', pecah_matrix[2])
u_total.append(pecah_matrix[2] - hitung_proyeksi(pecah_matrix[2],e_total[0]) - hitung_proyeksi(pecah_matrix[2],e_total[1]))
print('u3 = ',u_total[2])
e_total.append(hitung_e(u_total[2]))
print('e3 = ', e_total[2])