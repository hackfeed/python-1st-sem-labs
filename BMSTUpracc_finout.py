""" Решение задачи проложения кратчайшей линейной компьютерной сети.

Данная программа решает задачу проложения кратчайшей по длине
линейной компьютерной сети, заданной координатами компьютеров в двумерном
пространстве. В качестве входных данных программа получает сет данных,
в котором может содержаться информация о нескольких компьютерных сетях.
В качестве выходных данных пользователь получает информацию о каждой сети
вида: какой из компьютеров необходимо соединить первым и с каким и длина
этого соединения.

Входные значения:

file_input - файл с входными значениями
---- N - число компьютеров в сети
---- coords_duo - координаты компьютера в сети

Выходные значения:

file_output - файл с выходными значениями
---- first_comp2connect - координаты присоединяющего компьютера
---- second_comp2connect - координаты присоединяемого компьютера
---- path_len - необходимая длина кабеля между 1 и 2 компьютером
---- result - общая длина кабеля, проложенного в данной сети

Промежуточные значения:

network_counter - счётчик сетей во входных данных
dist_covered - матрица расстояний от каждого компьютера в сети
к каждому
coords_list - список координат компьютеров в сети
coords_duo - пара X-Y координат компьютера
result_way - порядок соединения компьютеров при котором будет затрачено
наименьшее количество проводов (по длине)
all_way_variants - все варианты соединения компьютеров в сети
total_dist_covered - длина затраченного провода для каждого из соединений
temp_records_list - список для итоговой записи результатов в файл
result_str, result_all_str - temp-переменные для вывода в файл
network_title - "название" сети
warning_message - предупреждающее сообщение при исключительных ситуациях

"""

import numpy as np
from itertools import permutations
from math import hypot

network_counter = 0

file_input = open("input.txt")

file_output = open("output.txt", "w")
file_output.write("")

while True:
    try:
        N = int(file_input.readline())

        if N == 0:
            file_output.close()
            file_input.close()
            break
        elif N < 0:
            file_output.write("Invalid data detected! Check your input!")
            file_output.close()
            file_input.close()
            break
        else:
            network_counter += 1

            """ Создание нулевой матрицы для последующего заполнения 
            длинами (реальными, без учёта издержек) расстояний между 
            компьютерами в сети. """
            dist_covered = np.zeros((N, N))
            coords_list = list()

            """ Заполнение списка координат компьютеров кортежами типа 
            (X_координата, Y_координата) """
            for i in range(N):
                coords_duo = tuple(map(int, file_input.readline().split()))
                coords_list.append(coords_duo)
            """ Заполнение матрицы расстояний между компьютерами в сети. 
            Расстояние находится по принципу прямоугольного треугольника. """
            for i in range(N):
                for j in range(i + 1, N):
                    dist_covered[i, j] = dist_covered[j, i] = hypot(
                        coords_list[i][0] - coords_list[j][0],
                        coords_list[i][1] - coords_list[j][1]
                    )

            result = dist_covered.sum() + 16*N
            result_way = None

            """ Функция permutations из модуля itertools отвечает за 
            количество возможных перестановок из аргумента. В данном 
            случае это список чисел от 0 до N-1. Таким образом мы 
            находим общее количество возможных способов соединить 
            N компьютеров в сети. Причём мы получаем не количество 
            этих способов, которое по правилам комбинаторики равняется 
            N!, а сами способы соединения. """
            all_way_variants = permutations(range(N))

            """ Выбрав какой-то из способов перестановок программа 
            начинает находить длину выбранного маршрута, обращаясь к 
            матрице расстояний, при этом добавляя издержки по количеству 
            проводов. """
            for current_way in all_way_variants:
                total_dist_covered = 0
                for i in range(1, N):
                    total_dist_covered += dist_covered[current_way[i-1],
                                                       current_way[i]] + 16
                if total_dist_covered < result:
                    result = total_dist_covered
                    result_way = current_way

            """ Подготовка выходных данных для записи в файл. """
            file_output = open("output.txt", "a+")

            temp_records_list = list()
            temp_records_list.append("*"*79 + "\n")
            network_title = "Network #" + str(network_counter) + "\n"
            temp_records_list.append(network_title)

            if N == 1:
                warning_message = ("The network consists only of 1 route\n" +
                                   "No cable required to maintain this\n")
                temp_records_list.append(warning_message)

            else:
                for i in range(1, N):
                    first_comp2connect = coords_list[result_way[i-1]]
                    second_comp2connect = coords_list[result_way[i]]
                    path_len = dist_covered[result_way[i-1], result_way[i]]+16
                    result_str = ("Cable requirement to connect "
                                  "{0} to {1} is {2:.2f} feet.\n".format(
                                   first_comp2connect, second_comp2connect,
                                   path_len))
                    temp_records_list.append(result_str)

                result_all_str = "Number of feet cable required is {0:.2f}\n".format(result)
                temp_records_list.append(result_all_str)

            file_output.writelines(temp_records_list)

    except ValueError:
        file_output.write("Invalid data detected! Check your input!")
        file_output.close()
        file_input.close()
        break
