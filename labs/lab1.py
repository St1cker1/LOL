from math import *  #импортировал математику


def task1():
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    z = float(input("Введите z: "))

    a = log1p(abs(x-1)) + abs(y**(1./3.))/(1 + x**(1./3.)) + sin(y) * sin(x)
    b = (abs(x - 1))**(1./3.) + cos(z) * tan(4 * x) + sinh(y)
    print(a, b)

def task2():
    x = float(input("Введите x: "))
    a = 3
    b = 2
    c = -2
    f = x ** b + sqrt(a*x)/c*x + a
    print(f)
def task3():
    x = float(input("Введите x: "))
    f = tanh(x)**2 * (abs(log(3, x**2)))
    print(f)

def task4():
    r = float(input("Введите: r "))
    h = float(input("Введите: h "))
    l = float(input("Введите: l"))
    R = 0

def task5():
    M = float(input("Введите M"))
    m = float(input("Введите m"))
    v = float(input("Введите v"))
    u = float(input("Введите u"))
    S = (m**2 * v**2)/(M**2 * 2 * 10 * u)
    print(S)

def task6():
    N = float(input("Введите N"))
    V1 = N * 4
    V2 = 1
    V = V1 - V2
    print(V)

def task7():
    A = float(input("Введите A от -100 до 100 не включая 0"))
    B = float(input("Введите B от -100 до 100"))
    X = -B/A
    print(X)

def task8():
    S = float(input("Введите S"))
    t = float(input("Введите t"))
    s = float(input("Введите s"))
    u = (S - s)/2 * t #скорость реки u
    v = (S + s)/2 * t #скорость лодки v
    print(u,v)

def task9():
    S = float(input("Введите S"))
    K = 1/100
    G = S * 36.54
    M = G - (G * K)
    print(M)

    task9()

