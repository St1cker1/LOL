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
    R =

task4()

