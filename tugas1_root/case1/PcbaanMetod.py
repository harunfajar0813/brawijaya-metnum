fx = lambda x: x**2 + 2*x + 1
a = float(input("Masukkan a: "))
b = float(input("Masukkan b: "))
if (fx(a)*fx((b))) < 0:
    while abs(fx(a)*fx(b)) > 0.0001:
        c = (a+b)/2
        if(fx(a)*fx(b) < 0.0):
            b = c
        else:
            a = c
        print("Akar persamaan adalah %f" % (c))
    else:
        print("penentuan a dan b salah")