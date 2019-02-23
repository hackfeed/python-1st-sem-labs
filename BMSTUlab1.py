""" Данная программа по введенным коэффициентам
A, B и C находит решения квадратного уравнения.

"""

from math import *
try:
    a, b, c = map(float, input("Введите коэффициенты A, B и C: ").split())
    print("(%sx^2)+(%sx)+(%s) = 0 - исходное уравнение" % (a, b, c))

    """ Проверка коэффициентов квадратного уравнения. """
    if a == 0:
        if b == 0:
            if c == 0:
                print("X - любое число")
            else:
                print("Нет решений")
        else:
            x = float(-c/b)
            print("%s - решение уравнения" % x)
    else:
        discr = float(b*b - 4*a*c)
        if discr == 0:
            xun = float(-b / (2*a))
            print("%s - корень данного уравнения" % xun)
        else:
            if discr > 0:
                x1 = float((-b - sqrt(discr)) / (2*a))
                x2 = float((-b + sqrt(discr)) / (2*a))
                print("%s, %s - корни данного уравнения" % (x1, x2))
            else:
                print("Мнимые корни")

except ValueError:
    print("Введены недопустимые значения")
