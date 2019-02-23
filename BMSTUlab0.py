"""  Данная программа вычисляет объём, площадь
боковой поверхности и площадь полной поверхности
усеченного конуса по его малому, большому радиусам
и высоте.

"""

from math import *
try:
    r_small, r_large, height = map(float, input("Введите малый радиус, большой радиус и высоту: ").split())

    if r_small == r_large:
        print("Вы ввели данные для цилиндра")
    elif r_small <= 0 or r_large <= 0 or height <= 0: 
        print("Введены недопустимые данные")
    else:
        v_cil = (height*pi*(r_large**2 + r_large*r_small + r_small**2))/3
        li = hypot(r_large-r_small, height)  # Находим образующую для последующих вычислений
        s_edge = pi*(r_small + r_large)*li
        s_full = pi*(r_small**2 + (r_small + r_large)*li + r_large**2)

        print("Объём: %s \n"
              "Площадь боковой поверхности: %s \n"
              "Площадь полной поверхности: %s" % (v_cil, s_edge, s_full))

except ValueError:
    print("Введены неверные значения (проверьте правильность ввода)")