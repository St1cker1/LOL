from math import *  #импортировал математику


def task1():
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    z = float(input("Введите z: "))

    a = log1p(abs(x-1)) + abs(y**(1./3.))/(1 + x**(1./3.)) + sin(y) * sin(x)
    b = (abs(x - 1))**(1./3.) + cos(z) * tan(4 * x) + sinh(y)
    print(a, b)


def task2():
    pass


task2()

