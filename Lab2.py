from math import *

import numpy as numpy


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
    a = float(input("Введите a "))
    b = float(input("Введите b "))
    for x in range(a, b):
        (x - e)**2 and 7*sin(x) + 9*cos(x)

def task3():
    a = int(input('Введите число '))
    b = int(input('Введите систему счисления'))
    d = 1
    while not d == 0:
        c = a % b
        print(c)
        d = a // b
        a = d

task3()
