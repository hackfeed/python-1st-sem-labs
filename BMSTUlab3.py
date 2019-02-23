""" Нахождение серии значений функции.

Данная программа определяет значение функции по заданной пользователем
серии аргументов (начало, шаг, конец), а также определяет в этой серии
наименьшее значение функции и значение аргумента, при котором функция
приняла наименьшее значение.

Входные данные:

t_start - начальный аргумент
t_step - приращение аргумента
t_end - конечный аргумент

Выходные данные:

w_min - минимальное значение функции
t_w_min - индекс минимального значения функции в списке всех значений

Промежуточные значения:

t_list - список для значений аргументов
w_list - список для значений функции
i - итератор для вывода номера
t - значение аргумента в определенный момент времени

Пример входных данных:

Введите начальное значение t, шаг и конечное значение t: -10 1 10

Пример выходных данных:

┏━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Номер ┃ Аргумент ┃ Значение W ┃
┃   1   ┃  -10.000 ┃  1.987e+15 ┃
┃   2   ┃   -9.000 ┃  5.573e+14 ┃
┃   3   ┃   -8.000 ┃  1.343e+14 ┃
┃   4   ┃   -7.000 ┃  2.665e+13 ┃
┃   5   ┃   -6.000 ┃  4.098e+12 ┃
┃   6   ┃   -5.000 ┃  4.426e+11 ┃
┃   7   ┃   -4.000 ┃  2.836e+10 ┃
┃   8   ┃   -3.000 ┃  7.684e+08 ┃
┃   9   ┃   -2.000 ┃  3.650e+06 ┃
┃  10   ┃   -1.000 ┃      1.000 ┃
┃  11   ┃    0.000 ┃      1.000 ┃
┃  12   ┃    1.000 ┃      1.000 ┃
┃  13   ┃    2.000 ┃  3.650e+06 ┃
┃  14   ┃    3.000 ┃  7.684e+08 ┃
┃  15   ┃    4.000 ┃  2.836e+10 ┃
┃  16   ┃    5.000 ┃  4.426e+11 ┃
┃  17   ┃    6.000 ┃  4.098e+12 ┃
┃  18   ┃    7.000 ┃  2.665e+13 ┃
┃  19   ┃    8.000 ┃  1.343e+14 ┃
┃  20   ┃    9.000 ┃  5.573e+14 ┃
┃  21   ┃   10.000 ┃  1.987e+15 ┃
┗━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━━━┛

Минимальное значение W = 1.000
Оно достигается при t = -1.000

"""
t_start, t_step, t_end = map(float,
                             input("Введите начальное значение t, "
                                   "шаг и конечное значение t: ").split())

print("┏━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━┓\n"
      "┃ Номер ┃ Аргумент ┃ Значение W ┃")

t_list = []
w_list = []
i = 1
t = t_start
if t > t_end:
    while t >= t_end:
        t_list.append(t)
        w_t = (2048 * t ** 12 - 6144 * t ** 10 + 6912 * t ** 8 -
               3584 * t ** 6 + 840 * t ** 4 - 72 * t ** 2 + 1)
        w_list.append(w_t)
        if abs(w_t) > 1e+4:
            print("┃{0:^7d}┃{1:9.3f} ┃{2:11.3e} ┃".format(i, t, w_t))
        else:
            print("┃{0:^7d}┃{1:9.3f} ┃{2:11.3f} ┃".format(i, t, w_t))
        t = round(t + t_step, 3)
        i += 1
    t_start, t_end = t_end, t_start
else:
    while t <= t_end:
        t_list.append(t)
        w_t = (2048 * t ** 12 - 6144 * t ** 10 + 6912 * t ** 8 -
               3584 * t ** 6 + 840 * t ** 4 - 72 * t ** 2 + 1)
        w_list.append(w_t)
        if abs(w_t) > 1e+4:
            print("┃{0:^7d}┃{1:9.3f} ┃{2:11.3e} ┃".format(i, t, w_t))
        else:
            print("┃{0:^7d}┃{1:9.3f} ┃{2:11.3f} ┃".format(i, t, w_t))
        t = round(t + t_step, 3)
        i += 1
print("┗━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━━━┛\n")

w_max = max(w_list)
w_min = min(w_list)
t_w_min = w_list.index(w_min)

if abs(w_min) > 1e+4:
    print("Минимальное значение W = {0:.3e}\n"
          "Оно достигается при t = {1:.3f}\n".format(w_min, t_list[t_w_min]))
else:
    print("Минимальное значение W = {0:.3f}\n"
          "Оно достигается при t = {1:.3f}\n".format(w_min, t_list[t_w_min]))

print("-"*79)
sequences_num = int(input("Введите количество засечек: "))
print("-"*79)

print()

line_len = (w_max-w_min)/sequences_num
tabs_num = 69//sequences_num
one_tab_len = line_len/tabs_num
d_wmaxmin = w_max - w_min

print("  {0:^10.3f}".format(w_min), end="")
cur = w_min + one_tab_len
f = 0
while f != sequences_num:
    if abs(cur) > 1e+4:
        print(" "*(tabs_num//2) + "{:^7.3e}".format(cur), end ="")
    else:
        print(" " * (tabs_num//2) + "{:^7.3f}".format(cur), end="")
    cur += one_tab_len
    f += 1
print()
print(" "*9 + "┏", end="")
k = 0
while k != sequences_num:
    print("━"*tabs_num + "┻", end="")
    k +=1
print("┓")

for x in range(len(t_list)):
    i = 0
    res = ""
    y_0 = False
    x_0_s = False
    if t_start + x*t_step <= 0 < t_start + (x + 1)*t_step:
        y_0 = True
    for i in range(0, 70):
        if y_0:
            if (w_min + i*d_wmaxmin/69 <= w_list[x] < w_min +
               (i + 1)*d_wmaxmin/69):
                res += "*"
            elif (w_min + i*d_wmaxmin/69 <= 0 < w_min +
                 (i + 1)*d_wmaxmin/69):
                res += "╋"
            else:
                res += "━"
        else:
            if (w_min + i*d_wmaxmin/69 <= w_list[x] < w_min +
               (i + 1)*d_wmaxmin/69):
                res += "*"
            elif (w_min + i*d_wmaxmin/69 <= 0 < w_min +
                 (i + 1)*d_wmaxmin/69):
                res += "┃"
                x_0 = i
                x_0_s = True
            else:
                res += " "
    if y_0:
        res += " Y"
    if x % 2 == 0:
        print("{0:^9.3f}".format(t_start + x*t_step) + "┃" + res)
    else:
        print(" "*9 + "┃" + res)
if x_0_s:
    print(" "*(9+x_0) + " X")