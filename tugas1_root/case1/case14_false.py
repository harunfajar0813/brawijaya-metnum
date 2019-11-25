# false position
import numpy as ny
import pylab as pb

def fungsi(x):
    return (x**10) - 1

def false_position(a,b):
    cp = a
    nomor = 1
    er = 10

    if (fungsi(a) * fungsi(b)) < 0:
        print("Iterasi\t   a\t    b\t      c\t       f(c)\t\t    Er\t")
        while abs(er) > 0.0001:
            c = b - (fungsi(b)*(a-b)) / (fungsi(a)-fungsi(b))
            cc = c
            er = ((cc - cp)/cc)*100
            print("%d\t\t%f  %f  %f  %f  %f" % (nomor, a, b, c, fungsi(c), abs(er)))
            cp = cc
            nomor += 1

            if (fungsi(a)*fungsi(c) < 0.0):
                b = c
            else:
                a = c
        print("akar adalah %f" % (c))
        print("\n")
    else:
        print("angka tidak valid")
        print("\n")
    return "program selesai dijalankan"

def graph(a,b):
    value = ny.arange(a, b, 0.0001)
    pb.axhline(y=0,color='r')
    pb.plot(value, fungsi(value))
    pb.grid(True)
    pb.show()

print(false_position(0.9,1.2),graph(0.9,1.2))
