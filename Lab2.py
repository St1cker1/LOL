def ends_with_even_digit(number):
    # Проверка, оканчивается ли число на четную цифру
    last_digit = int(str(number)[-1])
    return last_digit % 2 == 0

def is_not_perfect_square(number):
    # Проверка, является ли число бесквадратным
    square_root = int(number ** 0.5)
    return square_root ** 2 != number

def task1():
    while True:
        try:
            # Получение числа от пользователя
            user_input = int(input("Введите число (или введите '0' для выхода): "))
            
            # Проверка числа с помощью двух функций
            if user_input == 0:
                # Выход из программы при вводе '0'
                break
            elif ends_with_even_digit(user_input):
                print(f"{user_input} оканчивается на четную цифру.")
            else:
                print(f"{user_input} не оканчивается на четную цифру.")
            
            if is_not_perfect_square(user_input):
                print(f"{user_input} является бесквадратным числом.")
            else:
                print(f"{user_input} не является бесквадратным числом.")
                
        except ValueError:
            print("Ошибка! Введите корректное число.")

# task1()
            
import numpy as np
import matplotlib.pyplot as plt

# Функция f(x)
def f(x):
    if x >= 0:
        return (x - np.e)**2
    else:
        return 7 * np.sin(x) + 9 * np.cos(x)

def task2():
    # Задаем диапазон значений x
    a = -5
    b = 5

    # Генерируем значения x в заданном диапазоне
    x_values = np.linspace(a, b, 1000)

    # Вычисляем значения функции f(x) для каждого x
    y_values = np.vectorize(f)(x_values)

    # Строим график
    plt.plot(x_values, y_values, label='f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# task2()


def number_in_new_numeral_system(number, base):
    # Переводит целое десятичное число в систему счисления с заданным основанием
    result = ""
    
    while number > 0:
        remainder = number % base
        result = str(remainder) + result
        number //= base
    
    return result if result else "0"

def task3():
    try:
        # Получение от пользователя числа и основания системы счисления
        decimal_number = int(input("Введите целое десятичное число: "))
        target_base = int(input("Введите основание системы счисления (больше 1): "))

        if target_base <= 1:
            print("Ошибка: Основание должно быть больше 1.")
            return

        # Перевод числа в выбранную систему счисления
        result = number_in_new_numeral_system(decimal_number, target_base)

        # Вывод результата
        print(f"Число {decimal_number} в системе счисления с основанием {target_base}: {result}")

    except ValueError:
        print("Ошибка: Введите корректное целое число и основание системы счисления.")

# task3()
        
import matplotlib.pyplot as plt
import numpy as np

def is_point_inside_rectangle(x, y, x_min, y_min, x_max, y_max):
    return x_min <= x <= x_max and y_min <= y <= y_max

def task4():
    # Определение координат прямоугольных областей
    rectangle1 = {'x_min': 1, 'y_min': 1, 'x_max': 5, 'y_max': 4}
    rectangle2 = {'x_min': 7, 'y_min': 2, 'x_max': 10, 'y_max': 6}

    try:
        # Ввод координат точки от пользователя
        x = float(input("Введите x-координату точки: "))
        y = float(input("Введите y-координату точки: "))

        # Проверка принадлежности точки к прямоугольным областям
        if is_point_inside_rectangle(x, y, **rectangle1):
            print("Точка принадлежит первой области.")
        elif is_point_inside_rectangle(x, y, **rectangle2):
            print("Точка принадлежит второй области.")
        else:
            print("Точка не принадлежит ни одной из областей.")

        # Визуализация областей и точки
        plt.plot([rectangle1['x_min'], rectangle1['x_min'], rectangle1['x_max'], rectangle1['x_max'], rectangle1['x_min']],
                 [rectangle1['y_min'], rectangle1['y_max'], rectangle1['y_max'], rectangle1['y_min'], rectangle1['y_min']], label='Область 1', color='blue')

        plt.plot([rectangle2['x_min'], rectangle2['x_min'], rectangle2['x_max'], rectangle2['x_max'], rectangle2['x_min']],
                 [rectangle2['y_min'], rectangle2['y_max'], rectangle2['y_max'], rectangle2['y_min'], rectangle2['y_min']], label='Область 2', color='green')

        plt.scatter(x, y, color='red', label='Точка')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Принадлежность точки прямоугольным областям')
        plt.legend()
        plt.grid(True)
        plt.show()

    except ValueError:
        print("Ошибка: Введите корректные координаты точки.")

# task4()

def find_floor(apartment_number, even_floor_apartments, odd_floor_apartments, malfunctioning_floors):
    # Определение, на каких этажах находятся квартиры
    if apartment_number % 2 == 0:
        floor_apartments = even_floor_apartments
    else:
        floor_apartments = odd_floor_apartments

    # Определение этажа, на который нужно ехать
    target_floor = floor_apartments.index(apartment_number) + 1

    # Проверка, находится ли этаж в списке сломанных
    if target_floor in malfunctioning_floors:
        print(f"Лифт сломан и не может приехать на этаж {target_floor}.")
        print("Выберите один из ближайших этажей:")
        nearby_floors = [floor for floor in floor_apartments if floor not in malfunctioning_floors]
        print(nearby_floors)
        chosen_floor = int(input("Введите номер ближайшего этажа: "))
        return chosen_floor
    else:
        return target_floor

def task5():
    try:
        # Ввод номера квартиры
        apartment_number = int(input("Введите номер квартиры: "))

        # Количество квартир на четных и нечетных этажах
        even_floor_apartments = list(range(2, 101, 2))
        odd_floor_apartments = list(range(1, 100, 2))

        # Этажи, на которые лифт не может ездить
        malfunctioning_floors = list(range(1, 101, 3))

        # Определение этажа, на который нужно ехать
        target_floor = find_floor(apartment_number, even_floor_apartments, odd_floor_apartments, malfunctioning_floors)

        print(f"Лифт едет на этаж {target_floor}.")

    except ValueError:
        print("Ошибка: Введите корректный номер квартиры.")

# task5()

def simulate_population_growth(herbivores, predators, weeks):
    for week in range(weeks):
        # Увеличение популяций на 10%
        herbivores *= 1.1
        predators *= 1.1

        # Смерть от старости
        herbivores *= 0.99
        predators *= 0.97

        # Хищники сокращают травоядных на 10% от их числа
        herbivores -= 0.1 * predators

        # Проверка, чтобы численность популяций не стала отрицательной
        herbivores = max(0, herbivores)
        predators = max(0, predators)

        # Вывод текущей информации о популяциях
        print(f'Неделя {week + 1}: Травоядные: {herbivores:.2f}, Хищники: {predators:.2f}')

        # Проверка на снижение численности популяций до нуля
        if herbivores == 0 or predators == 0:
            print("Одна из популяций вымерла. Симуляция завершена.")
            break

def task6():
    try:
        # Ввод начальных значений популяций и количества недель
        initial_herbivores = float(input("Введите начальное количество травоядных: "))
        initial_predators = float(input("Введите начальное количество хищников: "))
        num_weeks = int(input("Введите количество недель для симуляции: "))

        # Запуск симуляции роста популяций
        simulate_population_growth(initial_herbivores, initial_predators, num_weeks)

    except ValueError:
        print("Ошибка: Введите корректные значения.")

# task6()
        
import math

def calculate_series_sum(x, n):
    series_sum = 0

    for i in range(n):
        term = (math.sin(x) ** (2 * i + 1)) / math.factorial(2 * i + 1)
        series_sum += term

    return series_sum

def task8():
    try:
        x = float(input("Введите значение x: "))
        n = int(input("Введите количество членов ряда для суммирования (n): "))

        result = calculate_series_sum(x, n)
        print(f"Сумма первых {n} членов ряда: {result:.6f}")

    except ValueError:
        print("Ошибка: Введите корректные значения.")

# task8()


