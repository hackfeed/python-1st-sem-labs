""" Вычисление интегралов методами численного интегрирования.

Данная программа вычисляет интеграл заданной функции методами численного
интегрирования, а именно методом трапеций и методом Уэддля. Для наименее
точного способа также вычисляется интеграл с заданной точностью.

Входные данные:

n1, n2 - исходные значения для разбиений
a_edge, b_edge - нижний и верхний пределы интегрирвоания
eps - точность для вычисления интеграла с заданной точностью

Выходные данные:

n1, n2 - см. выше
int_trap1, int_trap2 - вычисленные методом трапеций интегралы с разбиениями n1 и n2
int_weedle1, int_weedle2 - аналогично для метода Уэддля

eps - точность для метода с заданной точностью
int_trap_eps - значение интеграла с заданной точностью для метода трапеций
int_Fx - точное значение интеграла

abs_error, otn_error - абсолютная и относительная ошибки

Промежуточные значения:

n_eps - количество шагов для метода с заданной точностью
h1, h2, h_eps - значения шагов для n1, n2, n_eps
x_i - текущее значение аргумента
k_list - список для коэффициентов для метода Уэддля
int_trap_eps_start - стартовое значение для сравнения для метода с точностью

Пример входных данных:

Введите два значения для разбиения (кратно 6): 18 90
Введите верхнюю и нижнюю границы интегрирования: 0 5

Вычисление интеграла с точностью для метода трапеций
Введите значение epsilon: 0.001

Пример выходных данных:

**********************************************************
|    Метод       |     n1 =   18     |     n2 =   90     |
|   Трапеций     |         41.7309671|         41.6692387|
|    Уэддля      |         41.6666667|         41.6666667|
**********************************************************

Значение интеграла, вычисленное с точностью 0.001 = 41.6669846,  достигнутое за 256 шагов
Точное значение интеграла = 41.6666667

Метод трапеций с заданной точностью:
Абсолютная ошибка = 0.0003179
Относительная ошибка = 0.0000076

Метод трапеций:
Абсолютная ошибка = 0.0643004 при 18 разбиениях, 0.0025720 при 90 разбиениях
Относительная ошибка = 0.0015432 при 18 разбиениях, 0.0000617 при 90 разбиениях

Метод Уэддля:
Абсолютная ошибка = 0.0000000 при 18 разбиениях, 0.0000000 при 90 разбиениях
Относительная ошибка = 0.0000000 при 18 разбиениях, 0.0000000 при 90 разбиениях

"""

from math import sin

n1, n2 = map(int, input("Введите два значения для разбиения (кратно 6): ")
             .split())
a_edge, b_edge = map(float, input("Введите верхнюю и "
                                  "нижнюю границы интегрирования: ").split())


""" Подынтегральная функция. """


def func_in(x):
    return sin(x)**2


if n1 < 1 or n2 < 1 or a_edge >= b_edge:
    print("Введены некорректные исходные данные!")
else:
    int_Fx = (1/3*(b_edge)**3 - 1/3*(a_edge)**3)

    h1 = (b_edge - a_edge)/n1
    h2 = (b_edge - a_edge)/n2

    int_trap1 = int_trap2 = 0

    for i in range(1, n1):
        x_i = a_edge + i*h1
        int_trap1 += func_in(x_i)

    for i in range(1, n2):
        x_i = a_edge + i*h2
        int_trap2 += func_in(x_i)

    int_trap1 = h1*(int_trap1 + (func_in(a_edge)+func_in(b_edge))/2)
    int_trap2 = h2*(int_trap2 + (func_in(a_edge)+func_in(b_edge))/2)

    if n1 % 6 != 0 or n2 % 6 != 0:
        print("Метод Уэддля работает только для разбиений, кратных 6! "
              "Соответствующие значения будут заменены нулями!")
        int_weedel1 = int_weedel2 = 0
    else:

        int_weedel1 = int_weedel2 = 0
        k_list = [1, 5, 1, 6, 1, 5, 1]

        for i in range(0, n1, 6):
            for j in range(7):
                x_i = a_edge + (i+j)*h1
                int_weedel1 += k_list[j]*func_in(x_i)

        for i in range(0, n2, 6):
            for j in range(7):
                x_i = a_edge + (i+j)*h2
                int_weedel2 += k_list[j]*func_in(x_i)

        int_weedel1 = 0.3*h1*int_weedel1
        int_weedel2 = 0.3*h2*int_weedel2

    print()
    print("*"*58)
    print("|    Метод       |     n1 = {0:4}     |     n2 = {1:4}     |"
          .format(n1, n2))
    print("|   Трапеций     |{0:19.7f}|{1:19.7f}|"
          .format(int_trap1, int_trap2))
    print("|    Уэддля      |{0:19.7f}|{1:19.7f}|"
          .format(int_weedel1, int_weedel2))
    print("*" * 58)
    print()

    print("Вычисление интеграла с точностью для метода трапеций")
    eps = float(input("Введите значение epsilon: "))
    print()
    
    n_eps = 1
    h_eps = (b_edge - a_edge) / n_eps
    int_trap_eps_start = h_eps*((func_in(a_edge)+func_in(b_edge))/2)
    while True:
        int_trap_eps = 0
        n_eps *= 2
        h_eps = (b_edge - a_edge) / n_eps
        for i in range(1, n_eps):
            x_i = a_edge + i*h_eps
            int_trap_eps += func_in(x_i)
        int_trap_eps = h_eps*((func_in(a_edge)+func_in(b_edge))/2 + int_trap_eps)
        if abs(int_trap_eps - int_trap_eps_start) < eps:
            break
        else:
            int_trap_eps_start = int_trap_eps

    print("Значение интеграла, вычисленное с точностью {0} = {1:.7f}, "
          " достигнутое за {2} шагов".format(eps, int_trap_eps, n_eps))        
    print("Точное значение интеграла = {0:.7f} \n".format(int_Fx))

    abs_error = abs(int_Fx - int_trap_eps)
    otn_error = abs((int_Fx - int_trap_eps)/int_Fx)
    print("Метод трапеций с заданной точностью: \n"
          "Абсолютная ошибка = {0:.7f} \n"
          "Относительная ошибка = {1:.7f} \n".format(abs_error, otn_error))

    abs_error1 = abs(int_Fx - int_trap1)
    otn_error1 = abs((int_Fx - int_trap1) / int_Fx)
    abs_error2 = abs(int_Fx - int_trap2)
    otn_error2 = abs((int_Fx - int_trap2) / int_Fx)
    print("Метод трапеций: \n"
          "Абсолютная ошибка = {0:.7f} при {1} разбиениях, "
          "{2:.7f} при {3} разбиениях \n"
          "Относительная ошибка = {4:.7f} при {1} разбиениях, "
          "{5:.7f} при {3} разбиениях \n"
          .format(abs_error1, n1, abs_error2, n2, otn_error1, otn_error2))

    abs_error1 = abs(int_Fx - int_weedel1)
    otn_error1 = abs((int_Fx - int_weedel1) / int_Fx)
    abs_error2 = abs(int_Fx - int_weedel2)
    otn_error2 = abs((int_Fx - int_weedel2) / int_Fx)
    print("Метод Уэддля: \n"
          "Абсолютная ошибка = {0:.7f} при {1} разбиениях, "
          "{2:.7f} при {3} разбиениях \n"
          "Относительная ошибка = {4:.7f} при {1} разбиениях, "
          "{5:.7f} при {3} разбиениях \n"
          .format(abs_error1, n1, abs_error2, n2, otn_error1, otn_error2))