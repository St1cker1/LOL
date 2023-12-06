from math import *

from sympy import symbols, Eq, solve


def task1():
    '''Текст задания'''
    x = int(input('Введите число '))
    if x % 2 == 0:
        print("Оканчивается на четную цифру")
    else:
        print("Не оканчивается на четную цифру")

    x = int(input("Введите число"))
    if (sqrt(x)) % 1 == 0:
            print('Квадратное число')
    else:
            print('Бесквадратное число')



def task2():
    def f(x):
        if x >= 0:
            return (x - e)**2
        elif x < 0:
            return 7 * sin(x) + 9 * cos(x)

    a = float(input("Введите a "))
    b = float(input("Введите b "))

    x=[]


    #plot matplotlib


def task3():
    a = int(input('Введите число '))
    b = int(input('Введите систему счисления'))
    d = 1
    while not d == 0:
        c = a % b
        print(c)
        d = a // b
        a = d

task2()
