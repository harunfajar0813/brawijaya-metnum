# bisection
import numpy as ny
import pylab as pb

def fungsi(x):
    return (x**10) - 1

def bisection(a,b):
    cp = a
    nomor = 1
    if (fungsi(a) * fungsi(b)) < 0:
        print("Iterasi\t   a\t    b\t      c\t       f(c)\t\t ")
        while abs(fungsi(a) * fungsi(b)) > 0.1:
            c = (a+b) / 2
            print("%d\t\t%f  %f  %f  %f" % (nomor, a, b, c, fungsi(c)))
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
    value = ny.arange(a, b, 0.1)
    pb.plot(value, fungsi(value))
    pb.plot(value, fungsi(value))
    pb.axhline(y=0, color='r')
    pb.grid(True)
    pb.show()

print(bisection(0.9,1.2),graph(0.9,1.2))
