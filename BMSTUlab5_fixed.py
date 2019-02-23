""" Нахождение первого экстремума в заданной последовательности чисел.

Данная программа находит первый экстремум в последовательности чисел,
заданных строкой. В начале обнаруживается первое попавшееся число,
которое отвечает за количество введенных символов, затем обнарживаются
первые два числа в последовательности для последующих операций, а уже
после числа обнаруживаются по одному и производятся сравнения для
нахождения экстремума.

Входные данные:

in_str - входная строка с количеством чисел и самой последовательностью

Выходные данные:

extremum - найденный экстремум

Промежуточные значения:

ex_first, ex_second - 1 и 2 числа до нововходящего в последовательности
current_num - каждое нововходящее число после нажожждения ex_first/second
result_str - обрабатываемое число в строковом типе
count_str - число введенных чисел в строковом типе
ex_first_found, ex_second_found - флаги о нахождении 1 и 2 числа до текущего
count_found - флаг о найденном числе чисел в строке
count_row - количество введенных чисел в строке
space_start - флаг об обнаружении пробела (сигнал для обработки строки)
p_temp, m_temp - временные значения для упорядоченности смены значений

Пример входных данных:

5 1 2 -3 4 1

Пример выходных данных:

Первый найденный экстремум = 2

"""

in_str = input()
in_str += " "
ex_first = ex_second = current_num = None
extremum = None

ex_first_found = False
ex_second_found = False
count_found = False
space_start = False
result_str = ""
count_str = ""
count_row = 2

for i in in_str:
    if count_found is False:
        if i != " ":
            count_str += i
        else:
            count_found = True
            count_str = int(count_str)
            space_start = True
            
    if count_found:
        if i != " ":
            result_str += i
            space_start = False
        else:
            space_start = True
        if space_start:
            if ex_first_found is False and result_str != "":
                ex_first = int(result_str)
                ex_first_found = True
                result_str = ""
            if (ex_first_found is True and ex_second_found is False
                    and result_str != ""):
                ex_second = int(result_str)
                ex_second_found = True
                result_str = ""
            if ex_first_found and ex_second_found and result_str != "":
                current_num = int(result_str)
                count_row += 1
                result_str = ""

            p_temp = ex_second
            m_temp = current_num

        if (ex_first is not None and ex_second is not None
                and current_num is not None):
            if (ex_first < ex_second > current_num
                    or ex_first > ex_second < current_num):
                extremum = ex_second
                break
            ex_first = p_temp
            ex_second = m_temp

if count_row != count_str:
    print("Введенное количество чисел не равно предполагаемому")
else:
    if extremum is None:
        print("В данной последовательности нет экстремума")
    else:
        print("Первый найденный экстремум = %d" % extremum)
