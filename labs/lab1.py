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
    def calculate_truncated_cone_radius(r, h, l):
    R = (l * r) / math.sqrt(l**2 - h**2) + r
    return R
    r = float(input("Введите: r "))
    h = float(input("Введите: h "))
    l = float(input("Введите: l"))
result = calculate_truncated_cone_radius(r, h, l)
print("Радиус усеченного конуса R равен:", result

def task5():
M = float(input("Введите M"))
m = float(input("Введите m"))
v = float(input("Введите v"))
u = float(input("Введите u"))
S = (m**2 * v**2)/(M**2 * 2 * 10 * u)
print(S)

def task6():
    N = float(input("Введите N"))
    def calculate_sphere_volume(r):
    return (4/3) * math.pi * (r**3)

def calculate_ratio_of_volumes(N):
    # Пусть r1 - радиус первой сферы, а r2 - радиус второй сферы
    # Тогда r1 = N * r2
    # Объемы шаров равны V1 = (4/3) * pi * r1^3 и V2 = (4/3) * pi * r2^3
    # V1/V2 = (r1/r2)^3 = N^3
    ratio = N**3
    return ratio
result = calculate_ratio_of_volumes(N)
print("Отношение V1/V2 равно:", result)

def task7():
    A = float(input("Введите A от -100 до 100 не включая 0"))
    B = float(input("Введите B от -100 до 100"))
    def solve_linear_equation(A, B):
    if A == 0:
        return "Уравнение не является линейным (A не может быть равно 0)"
    else:
        x = -B / A
        return round(x, 4)
result = solve_linear_equation(A, B)
print("Корень уравнения равен:", result)

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

    task1()

