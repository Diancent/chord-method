import math
from sympy import *
import numpy as np

x = symbols('x')

def f(x):
    return x ** 2 - cos(math.pi * x)

def chord_method(equation, a, b, e):
    print(f"Значення F(a): {f(a)}")
    print(f"Значення F(b): {f(b)}")
    print()

    # первірка чи існує хочаб 1 корінь
    if f(a) * f(b) > 0:
        raise Exception("Похибка початкового наближення")

    print(diff(x ** 2 - cos(np.pi * x)))

    derivative_F = diff(x ** 2 - cos(np.pi * x), x)

    derivative_values = [derivative_F.subs(x, point) for point in [a, b]]

    # первірка чи існує більше 1 кореня
    if derivative_values[0] * derivative_values[1] < 0:
        raise Exception("На вказаному відрізку більше одного кореня.")

    k = 0

    # Визначення нерухомого кінця якщо true то b нерухома точка. Похідна з а *  похідну з а другого порядка > 0
    n = a

    derivative_expr_1 = diff(x ** 2 - cos(np.pi * x), x)
    print(f"Аналітичний вираз похідної: {derivative_expr_1}")

    derivative_1 = derivative_expr_1.subs(x, n)
    print(f"Значення похідної при x = {n}: {derivative_1}")

    derivative_expr_2 = diff(derivative_expr_1, x)
    print(f"Аналітичний вираз похідної: {derivative_expr_2}")

    derivative_2 = derivative_expr_2.subs(x, n)
    print(f"Значення похідної при x = {n}: {derivative_2}")

    if derivative_1 * derivative_2 > 0:
        z = a
        a = b
        b = z
        print("b - нерухома точка")

    else:
        print("a - нерухома точка")

    c1 = a

    while True:
        a_values = a ** 2 - math.cos(np.pi * a)
        b_values = b ** 2 - math.cos(np.pi * b)

        c2 = a - (a_values * (b-a))/(b_values-a_values)
        print(c2)
        c_values = c2 ** 2 - math.cos(np.pi * c2)

        k += 1
        if abs(c2-c1) < e:
            print(f"{k} ітерація")
            print(c2)
            return c2

        if (a_values < 0 < c_values) or (a_values > 0 > c_values):
            b = c2
        else:
            a = c2

        c1 = c2
        print(f"{k} ітерація")

if __name__ == '__main__':
    a = 0
    b = 1
    e = 10e-6

    chord_method(f,a,b,e)
