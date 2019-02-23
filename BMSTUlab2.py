""" Вычисление параметров треугольника, имея координаты его вершин.

Данная программа определяет длины сторон треугольника по заданным
координатам вершин, находит длину высоты, проведенной из большего
угла, определяет треугольник на прямоугольность, определяет,
находится ли дополнительная точка R внутри треугольника и если да
то вычисляет длину расстояния до наиболее удалённой стороны, а
также проверяет треугольник на существование.

"""

""" Входные данные:
apoint_x, apoint_y - координата x и y соответственно точки A
bpoint_x, bpoint_y - координата x и y соответственно точки B
cpoint_x, cpoint_y - координата x и y соответственно точки C
rpoint_x, rpoint_y - координата x и y соответственно точки R

"""

""" Выходные данные:
ab_length - длина стороны AB
bc_length - длина стороны BC
ac_length - длина стороны AC

max_angle - наибольший угол в треугольнике ABC (буква)
h_max - длина высоты, проведенной из наибольшего угла

max_dist - расстояние от точки R до наиболее удалённой стороны
faraway_side - наиболее удалённая сторона

"""

""" Промежуточные значения: 
abvect_x - координата X вектора AB
abvect_y - координата Y вектора AB
acvect_x - координата X вектора AC
acvect_y - координата Y вектора AC
bcvect_x - координата X вектора BC
bcvect_y - координата Y вектора BC

abbc_prod_abs - абсолютное значение произведения векторов AB и BC
abac_prod_abs - абсолютное значение произведения векторов AB и AC
bcac_prod_abs - абсолютное значение произведения векторов BC и AC

a_angle_cos - значение косинуса угла A
a_angle_sin - значение синуса угла A

square_abc_signed - значение площади треугольника ABC/(0.5)
max_side - длина наибольшей стороны треугольника ABC

min_prod - минимальное абсолютное значение произведения векторов в ABC

coeff_1, coeff_2, coeff_3 - коэффициенты псевдоскалярного произведения

ab_a, ab_b, ab_c - коэффициенты в уравнении прямой AB
ac_a, ac_b, ac_c - коэффициенты в уравнении прямой AC
bc_a, bc_b, bc_c - коэффициенты в уравнении прямой BC

dist_1, dist_2, dist_3 - расстояния от точки R до прямых AB, AC и BC соотв.

"""

""" Пример входных данных (1) (ABC - существует, прямоугольный, R - внутри): 

Введите координаты точки А: 0 0
Введите координаты точки B: 0 4
Введите координаты точки C: 3 0
Введите координаты точки R: 1 1

Пример выходных данных:

-------------------------------
Длины сторон: 
• AB = 4.00 
• BC = 5.00 
• AC = 3.00
A - наибольший угол. Длина высоты из угла A = 2.40
Треугольник ABC - прямоугольный
Точка R принадлежит треугольнику
1.00 - расстояние до AB (максимально удалённой стороны)


Пример входных данных (2) (ABC - существует, прямоугольный, R - извне):

Введите координаты точки А: 0 0
Введите координаты точки B: 0 4
Введите координаты точки C: 3 0
Введите координаты точки R: 3 1

Пример выходных данных:

-------------------------------
Длины сторон: 
• AB = 4.00 
• BC = 5.00 
• AC = 3.00
A - наибольший угол. Длина высоты из угла A = 2.40
Треугольник ABC - прямоугольный
Точка R лежит вне треугольника

Пример входных данных (3) (ABC - существует, произвольный, R - внутри):

Введите координаты точки А: 0 0
Введите координаты точки B: 4 0
Введите координаты точки C: 3 2
Введите координаты точки R: 3 1

Пример выходных данных:

-------------------------------
Длины сторон: 
• AB = 4.00 
• BC = 2.24 
• AC = 3.61
C - наибольший угол. Длина высоты из угла C = 2.00
Треугольник ABC - непрямоугольный
Точка R принадлежит треугольнику
1.00 - расстояние до AB (максимально удалённой стороны)

Пример входных данных (4) (ABC - существует, произвольный, R - извне):

Введите координаты точки А: 0 0
Введите координаты точки B: 4 0
Введите координаты точки C: 3 2
Введите координаты точки R: 3 3

Пример выходных данных:

-------------------------------
Длины сторон: 
• AB = 4.00 
• BC = 2.24 
• AC = 3.61
C - наибольший угол. Длина высоты из угла C = 2.00
Треугольник ABC - непрямоугольный
Точка R лежит вне треугольника

Пример входных данных (5) (ABC - не существует):

Введите координаты точки А: 1 1
Введите координаты точки B: 2 2
Введите координаты точки C: 3 3
Введите координаты точки R: 5 6

Пример выходных данных:

-------------------------------
Три точки лежат на одной прямой, треугольник не существует

"""

from math import *
apoint_x, apoint_y = map(int, input("Введите координаты точки А: ").split())
bpoint_x, bpoint_y = map(int, input("Введите координаты точки B: ").split())
cpoint_x, cpoint_y = map(int, input("Введите координаты точки C: ").split())
rpoint_x, rpoint_y = map(int, input("Введите координаты точки R: ").split())

print("-------------------------------")

if ((cpoint_x - apoint_x) * (cpoint_y - bpoint_y) ==
   (cpoint_y - apoint_y) * (cpoint_x - bpoint_x)):
    print("Три точки лежат на одной прямой, треугольник не существует")
else:
    ab_length = sqrt((apoint_x - bpoint_x)**2 + (apoint_y - bpoint_y)**2)
    ac_length = sqrt((apoint_x - cpoint_x)**2 + (apoint_y - cpoint_y)**2)
    bc_length = sqrt((cpoint_x - bpoint_x)**2 + (cpoint_y - bpoint_y)**2)

    print("Длины сторон: \n"
          "• AB = {0:.2f} \n"
          "• BC = {1:.2f} \n"
          "• AC = {2:.2f}". format(ab_length, bc_length, ac_length))

    abvect_x = bpoint_x - apoint_x
    abvect_y = bpoint_y - apoint_y

    acvect_x = cpoint_x - apoint_x
    acvect_y = cpoint_y - apoint_y

    bcvect_x = cpoint_x - bpoint_x
    bcvect_y = cpoint_y - bpoint_y

    abbc_prod_abs = abs((abvect_x * bcvect_x) + (abvect_y * bcvect_y))
    abac_prod_abs = abs((abvect_x * acvect_x) + (abvect_y * acvect_y))
    bcac_prod_abs = abs((bcvect_x * acvect_x) + (bcvect_y * acvect_y))

    a_angle_cos = ((ab_length**2 + ac_length**2 - bc_length**2) /
                   (2*ab_length*ac_length))
    a_angle_sin = sqrt(1 - a_angle_cos**2)
    square_abc_signed = ab_length*ac_length*a_angle_sin
    max_side = max(ab_length, ac_length, bc_length)

    if max_side == ab_length:
        max_angle = "C"
    elif max_side == ac_length:
        max_angle = "B"
    else:
        max_angle = "A"

    h_max = square_abc_signed/max_side
    print("{0} - наибольший угол. Длина высоты из угла {0} = {1:.2f}".
          format(max_angle, h_max))

    min_prod = min(abbc_prod_abs, abac_prod_abs, bcac_prod_abs)

    if min_prod == 0:
        print("Треугольник ABC - прямоугольный")
    else:
        print("Треугольник ABC - непрямоугольный")

    coeff_1 = ((apoint_x - rpoint_x)*(bpoint_y - apoint_y) -
               (bpoint_x - apoint_x)*(apoint_y - rpoint_y))
    coeff_2 = ((bpoint_x - rpoint_x)*(cpoint_y - bpoint_y) -
               (cpoint_x - bpoint_x)*(bpoint_y - rpoint_y))
    coeff_3 = ((cpoint_x - rpoint_x)*(apoint_y - cpoint_y) -
               (apoint_x - cpoint_x)*(cpoint_y - rpoint_y))

    if (coeff_1 >= 0 and coeff_2 >= 0 and coeff_3 >= 0 or
       coeff_1 <= 0 and coeff_2 <= 0 and coeff_3 <= 0):
        print("Точка R принадлежит треугольнику")

        ab_a = abvect_y
        ab_b = -abvect_x
        ab_c = apoint_x*(-ab_a) + apoint_y*(-ab_b)

        ac_a = acvect_y
        ac_b = -acvect_x
        ac_c = apoint_x*(-ac_a) + apoint_y*(-ac_b)

        bc_a = bcvect_y
        bc_b = -bcvect_x
        bc_c = bpoint_x*(-bc_a) + bpoint_y*(-bc_b)

        dist_1 = (abs(ab_a*rpoint_x + ab_b*rpoint_y + ab_c) /
                  sqrt(ab_a**2 + ab_b**2))
        dist_2 = (abs(ac_a*rpoint_x + ac_b*rpoint_y + ac_c) /
                  sqrt(ac_a**2 + ac_b**2))
        dist_3 = (abs(bc_a*rpoint_x + bc_b*rpoint_y + bc_c) /
                  sqrt(bc_a**2 + bc_b**2))

        max_dist = max(dist_1, dist_2, dist_3)

        if max_dist == dist_1:
            faraway_side = "AB"
        elif max_dist == dist_2:
            faraway_side = "AC"
        else:
            faraway_side = "BC"

        print("{0:.2f} - расстояние до {1} (максимально удалённой стороны)".
              format(max_dist, faraway_side))
    else:
        print("Точка R лежит вне треугольника")
