import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-3,3,0.001)
y= x** 4 - 2 *( x ** 2) + x - 3
fx = lambda x: x ** 4 - 2 *( x ** 2) + x - 3

# memasukan inputran user



def Brent(a, b, Es):
    a = 1.0
    b = 3.0
    fa = fx(a)
    fb = fx(b)
    Es = 0.001
    Er = 100.0
    if abs(fa) < abs(fb):
        a, b = b, a
        fa, fb = fb, fa
    c = a
    fc = fx(c)
    fc = fa
    c0ld = 0
    loop = 0
    bisection = True
    print("n\t   a\t\t    b\t\t    s\t\t    fa\t\t    fb\t\t      Er")
    while abs(b - a) > Es:
        fa = fx(a)
        fb = fx(b)
        fc = fx(c)
        if fx(a) != fx(c) and fx(b) != fx(c):
            L0 = (a * fa * fc) / ((fa - fb) * (fa - fc))
            L1 = (b * fb * fc) / ((fb - fa) * (fb - fc))
            L2 = (c * fc * fa) / ((fc - fa) * (fc - fb))
            s = L0 + L1 + L2

        else:
            s = b - fb * ((b - a) / fb - fa)
        if ((s < ((3 * a + b) / 4) or s > a) or
                (bisection == True and (abs(s - b)) >= (abs(b - c) / 2)) or
                (bisection == False and (abs(s - b)) >= (abs(c - d) / 2)) or
                (bisection == True and (abs(b - c)) < Es) or
                (bisection == False and (abs(c - d)) < Es)):
            s = (a + b) / 2
            bisection == True
        else:
            bisection == False
        cNew = s
        Er = abs((a - b) / a)
        print("%d\t%f\t%f\t%f\t%f\t%f\t%f" % (loop + 1, a, b, s, fx(a), fx(b), Er))
        c0old = cNew
        fs = fx(s)
        d, c = c, b
        if (fa * fs < 0):
            b = s
            print(loop,'. b = ',b)
        else:
            a = s
            print(loop,'. a = ',a)
        if abs(fa) < abs(fb):
            [a, b] = [b, a]
        loop += 1
        plt.plot(b, fx(b), '.')
    print(" ")
    print("Akar persamaan : %.5f" % (s))
    print("Iterasi : %d" % (loop))




def main():
    a = 0
    b = 0
    Es = 0
    a, b, Es = a, b, Es
    Brent(a, b, Es)


main()
plt.title("Metode Brent")
plt.plot(x,y,'-')
plt.axhline(y=0,color='r')
plt.show()