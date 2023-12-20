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


def task5():
    def find_floor(n, k):
    apartment_number = int(input("Введите номер квартиры: "))

    if apartment_number < 1 or apartment_number > n * k:
        print("Ошибка! Неверный номер квартиры.")
        return

    floor = (apartment_number - 1) // k + 1

    if floor % 3 == 0:
        print("Лифт не может ехать на этот этаж.")
        print("Выберите один из ближайших этажей:")
        nearest_floors = [floor - 1, floor + 1]
        for nearest_floor in nearest_floors:
            if nearest_floor % 3 != 0:
                print(nearest_floor)
        return

    print("Лифт едет на этаж:", floor)

def task6():
    def calculate_population(weeks, herbivores, predators):
    for week in range(1, weeks + 1):
        print("Неделя", week)
        print("Травоядные:", herbivores)
        print("Хищники:", predators)
        
        herbivores -= herbivores * 0.01  # Уменьшение популяции травоядных на 1% в месяц
        predators -= predators * 0.03  # Уменьшение популяции хищников на 3% в месяц
        
        herbivores -= predators * 0.1  # Сокращение популяции травоядных на 10% от числа хищников
        
        if herbivores <= 0:
            print("Популяция травоядных исчезла")
            break
        if predators <= 0:
            print("Популяция хищников исчезла")
            break

weeks = int(input("Введите количество недель: "))
herbivores = int(input("Введите начальное количество травоядных: "))
predators = int(input("Введите начальное количество хищников: "))

calculate_population(weeks, herbivores, predators)
def task8():
    n = int(input("Введите n "))
    x = int(input("Введите x "))
    for i in range(1, n+1):
        s = s +((sin(x))**(2 * i - 1)/(2i - 1)
                print(s)
    
    
 
