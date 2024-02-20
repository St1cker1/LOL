import math

def task1(x, y, z):
    a = math.log(math.sqrt(abs(x - 1)) + pow(abs(y), 1/3) / (math.sqrt(1 + x**2) + math.sin(y) * math.sin(x)))
    b = pow(abs(x - 1), 1/3) + math.cos(z) * math.tan(4 * x) + math.sinh(y)
    return a, b

# Пример использования:
x_val = 2
y_val = -1
z_val = 0.5

result_a, result_b = task1(x_val, y_val, z_val)
print(f"Результаты вычислений: a = {result_a}, b = {result_b}")


def task2(x):
    a = 3
    b = 2
    c = -2
    result = x**b + (math.sqrt(a*x) / (c*x + a))
    return result

# Пример использования:
x_val = 4.5  # Произвольное значение x
result_f = task2(x_val)
print(f"Значение функции f({x_val}) = {result_f}")


def task3(x):
    result = math.tanh(x)**2 * abs(math.log(x**2, 3))
    return result

x_val = 1.5  # Произвольное значение x
result_f = task3(x_val)
print(f"Значение функции f({x_val}) = {result_f}")


def find_truncated_cone_radius(r, l):
    R = math.sqrt(r**2 + l**2)
    return R

def task4(radius_upper_base,slant_height):
    result_radius = find_truncated_cone_radius(radius_upper_base, slant_height)
    return result_radius

result_f  = task4(3,4)
print(f"Радиус основания R усеченного конуса: {result_f}")

def task5(M, m, v, friction_coefficient):
    g = 9.8  # ускорение свободного падения
    friction_force = friction_coefficient * M * g
    distance = (m * v**2) / (friction_force)
    return distance

M = 70  # масса конькобежца в кг
m = 0.5  # масса камня в кг
v = 10  # скорость броска в м/с
friction_coefficient = 0.2  # коэффициент трения
result_distance = task5(M, m, v, friction_coefficient)
print(f"Расстояние, на которое откатится конькобежец: {result_distance} м")

def task6(N):
    V2_V_ratio = 1 / (N**3)
    return V2_V_ratio

N = 2  # отношение радиусов сфер
result_ratio = task6(N)
print(f"Отношение объема тела между сферами к объему второй сферы: {result_ratio}")


def task7(A, B):
    x = -B / A
    return round(x, 4)

# Пример использования:
A = 2
B = -8
result_root = task7(A, B)
print(f"Корень уравнения Ax + B = 0: {result_root}")

def task8(S, t, s):
    river_speed = (S + s) / t
    boat_speed = (s / t) + river_speed
    return river_speed, boat_speed

# Пример использования:
S = 10  # расстояние до пристани
t = 2  # время до поселка
s = 5  # расстояние от поселка до плота
result_river_speed, result_boat_speed = task8(S, t, s)
print(f"Скорость течения реки: {result_river_speed} км/ч, Скорость лодки относительно воды: {result_boat_speed} км/ч")

def task9(dollars, commission_rate):
    converted_amount = dollars * (1 - commission_rate)
    return round(converted_amount, 4)

# Пример использования:
dollars_amount = 100  # сумма в долларах
commission_rate = 0.02  # комиссия 2%
result_griwnas = task9(dollars_amount, commission_rate)
print(f"Сумма в гривнах после конвертации: {result_griwnas} грн")
