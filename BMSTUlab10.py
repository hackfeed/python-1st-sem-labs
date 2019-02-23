""" Выполнение действий над текстом, выбираемых пользователем.

Данная программа позволяет произвести над исходным текстом такие
операции, как: выравнивание по ширине, выравнивание по левому краю,
выравнивание по правому краю, замена во всём тексте одного слова
другим , удаление заданного слова из текста, замена арифметических
выражений, состоящих из умножения и деления, на результат их
вычисления. Все эти операции пользователь может выбрать в меню,
которое появляется при каждом новом запуске программы или окончании
последнего запрошенного действия.

Входные данные:

input_text - текст, над которым выполняются операции

Выходные данные:

sentence - построчное представление текста

Подробную документацию по каждой из функции см. в коде далее

"""

input_text = [" Миллиган медленно встал и пошел в спальню. Встав у двери, ",
              "он кивнул в сторону небольшой картонной коробки, стоявшей",
              "         возле комода. Клеберг  остался с ним, а Боксербаум вернулся      ",
              "  в гостиную. Остальные офицеры столпились         в дверном проеме",
              "               позади Миллигана. Боксербаум опустился на колени возле",
              "    коробки. Через отверстие сверху в ней виднелись провода",
              "и нечто, похожее на часы."]

print("ИСХОДНЫЙ ТЕКСТ")
for sentence in input_text:
    print(sentence)
print()

input_text[len(input_text)-1] += " "


def menu_title():
    """ Вызов меню. Функция позволяет пользователю выбрать операцию
    из списка для выполнения выбранной над текстом.

    Входные/выходные данные:

    menu_number - выбранный номер из меню (возвращается в случае
    выполнения функции без ошибок) """
    while True:
        print("  Операции с текстом\n"
              "1. Выравнивание по ширине\n"
              "2. Выравнивание по левому краю\n"
              "3. Выравнивание по правому краю\n"
              "4. Замена во всём тексте одного слова другим\n"
              "5. Удаление заданного слова из текста\n"
              "6. Замена арифметических операций на их числовое значение\n"
              "7. Вывод предложений, в которых максимальное количество слов "
              "заданной длины\n"
              "8. Нахождение предложения с максимальным количеством слов, "
              "содержащих заданную букву\n"
              "9. Удалить самое длинное слово в самом длинном по числу слов "
              "предложении\n"
              "\n"
              "0. Выход\n")

        try:
            menu_number = int(input("Введите номер операции: "))
            print()

            if menu_number > 9 or menu_number < 0:
                print("Операции с данным номером не существует!\n")
            else:
                return menu_number
                
        except ValueError:
            print("Введены некорректные данные\n")


def text_preparation(in_text):
    """ Предобработка текста перед выполнением программы.
    Функция удаляет все пробелы слева, справа текста, а также
    излишние пробелы между словами внутри текста.

    Входные/выходные данные:

    in_text - текст, полученный на обработку (возвращается по
    выполнению функции) """
    in_text_new = [0]*len(in_text)
    for i in range(len(in_text)):
        str_list = in_text[i].split()
        in_text_new[i] = " ".join(str_list)
    return in_text_new


def weight_alignment(in_text):
    """ Выравнивание по ширине. Функция выравнивает текст по ширине
    по принципу добавления пробелов к каждому из исходных пробелов
    по очереди до достижения строкой максимальной строки в исходном
    тексте.

    Входные данные:

    in_text - текст (массив строк), полученный на обработку

    Промежуточные значения:

    max_len_sen - длина максимальной строки в тексте
    space_counter - количество пробелов в рассматриваемой строке
    needed_spaces - необходимое количество пробелов для дополнения
    строки до максимальной длины
    space_list - массив для необходимого количества дополнительных
    пробелов для каждого из пробелов
    all_spaces - количество дополнительных пробелов, которого хватит
    для всех исходных пробелов
    left_spaces - количество оставшихся пробелов, которые необходимо
    равномерно распределить по первым пробелам
    space_pos - индексы пробелов в строке (от 0 до space_count-1)

    Выходные данные:

    res_str - полученная строка шириной max_len_sen """
    max_len_sen = 0
    # Поиск максимально длинной строки
    for i in range(len(in_text)):
        if len(in_text[i]) > max_len_sen:
            max_len_sen = len(in_text[i])
    for i in range(len(in_text)):
        res_str = ""
        if len(in_text[i]) < max_len_sen:
            # Нахождение общего числа пробелов в строке
            # а также количества дополнительных пробелов
            space_counter = 0
            needed_spaces = max_len_sen - len(in_text[i])
            for j in range(len(in_text[i])):
                if in_text[i][j] == " ":
                    space_counter += 1
            space_list = [0]*space_counter
            all_spaces = needed_spaces // space_counter
            left_spaces = needed_spaces % space_counter
            # Формирование списка, в котором хранится
            # итоговое (учитывая один "стартовый")
            # количество пробелов для каждого разделения
            for k in range(space_counter):
                space_list[k] = all_spaces+1
            l = 0
            while left_spaces > 0:
                space_list[l] += 1
                left_spaces -= 1
                l += 1
            # Формирование итоговой строки длиной max_len_sen
            space_pos = 0
            for j in range(len(in_text[i])):
                if in_text[i][j] != " ":
                    res_str += in_text[i][j]
                else:
                    res_str += " "*space_list[space_pos]
                    space_pos += 1
            print(res_str)
        else:
            print(in_text[i])
    print()


def left_edge_alignment(in_text):
    """ Выравнивание по левому краю. Функция выравнивает текст
    по левому краю по принципу удаления всех пробелов перед
    первым словом в каждой строке.

    Входные данные:

    in_text - текст (массив строк), полученный на обработку

    Промежуточные значения:

    symbol_found - флаг первого вхождения непробельного символа
    в строке

    Выходные данные:

    res_str - полученная строка """
    for i in range(len(in_text)):
        symbol_found = False
        res_str = ""
        for j in range(len(in_text[i])):
            if in_text[i][j] != " ":
                symbol_found = True
            if symbol_found:
                res_str += in_text[i][j]
        print(res_str)
    print()


def right_edge_alignment(in_text):
    """ Выравнивание по правому краю. Фунцкия выравнивает текст
    по правому краю по приницпу добавления пробелов перед первым
    словом в каждой строке до момента, пока её длина не сравнится
    с длиной максимальной строки в тексте.

    Входные данные:

    in_text - текст (массив строк), полученный на обработку

    Промежуточные значения:

    max_len_sen - длина максимальной строки в тексте
    needed_space - необходимое количество пробелов для строки, чтобы
    ее длина стала max_len_sen

    Выходные данные:

    res_str - полученная строка """
    max_len_sen = 0
    # Поиск максимально длинной строки
    for i in range(len(in_text)):
        if len(in_text[i]) > max_len_sen:
            max_len_sen = len(in_text[i])
    # Поиск дополнительных пробелов для данной строки
    # а также формирование итоговой строки
    for i in range(len(in_text)):
        if len(in_text[i]) != max_len_sen:
            needed_spaces = max_len_sen - len(in_text[i])
            res_str = " "*needed_spaces + in_text[i]
            print(res_str)
        else:
            print(in_text[i])
    print()


def replacer(in_text):
    """ Замена во всём тексте одного слова другим.

    Входные данные:

    in_text - текст (массив строк), полученный на обработку
    replace_word_in - слово в тексте, которое необходимо заменить
    replace_word_out - на какое слово нужно заменить исходное

    Промежуточные значения:

    str_list - список слов в строке
    str_list_end - матрица слов исходного текста

    Выходные данные:

    res_str - полученная строка """
    replace_word_in = input("Введите исходное слово для замены: ")
    replace_word_out = input("Введи слово, которое заменит исходное слово: ")
    str_list_end = []
    for sen in in_text:
        str_list = sen.split()
        str_list_end.append(str_list)
        for i in range(len(str_list)):
            # Проверка на совпадение каждого из слов в строке
            # с заданным словом
            if str_list[i].lower() == replace_word_in.lower():
                # Замена слова с учётом регистра
                if str_list[i-1][len(str_list[i-1])-1] != ".":
                    str_list[i] = replace_word_out
                else:
                    str_list[i] = (replace_word_out[0].upper() +
                                   replace_word_out[1:])
    # Форматированный вывод
    for i in range(len(in_text)):
        k = 0
        res_str = ""
        for j in range(len(in_text[i])):
            if in_text[i][j] == " ":
                res_str += " "
            elif in_text[i][j] != " " and in_text[i][j-1] == " ":
                res_str += str_list_end[i][k]
                k += 1
        if in_text[i][0] != " " and res_str[0] == " ":
            res_str = res_str[1:]
        print(res_str)
    print()


def deleter(in_text):
    """ Удаление заданного слова из текста.

    Входные данные:

    in_text - текст (массив строк), полученный на обработку
    delete_word_in - слово в тексте, которое необходимо удалить

    Промежуточные значения:

    str_list - список слов в строке
    str_list_end - матрица слов исходного текста

    Выходные данные:

    res_str - полученная строка """
    delete_word_in = input("Введите исходное слово для удаления: ")
    str_list_end = []
    for sen in in_text:
        str_list = sen.split()
        str_list_end.append(str_list)
        for i in range(len(str_list)):
            if str_list[i].lower() == delete_word_in.lower():
                str_list[i] = ""
    # Форматированный вывод
    for i in range(len(in_text)):
        k = 0
        res_str = ""
        for j in range(len(in_text[i])):
            if in_text[i][j] == " ":
                res_str += " "
            elif in_text[i][j] != " " and in_text[i][j - 1] == " ":
                res_str += str_list_end[i][k]
                k += 1
        if in_text[i][0] != " " and res_str[0] == " ":
            res_str = res_str[1:]
        print(res_str)
    print()


def evaler(in_text):
    """ Замена арифметических операций в тексте на результат
    их вычисления.

    Входные данные:

    in_text - текст (массив строк), полученный на обработку

    Промежуточные значения:

    str_list - список слов в строке
    str_list_end - матрица слов исходного текста

    Выходные данные:

    res_str - полученная строка """
    str_list_end = []
    for sen in in_text:
        str_list = sen.split()
        str_list_end.append(str_list)
        for i in range(len(str_list)):
            # Если найденное слово - арифметическое
            # выражение - результат будет получен
            try:
                str_list[i] = str(eval(str_list[i]))
            except:
                pass
    # Форматированный вывод
    for i in range(len(in_text)):
        k = 0
        res_str = ""
        for j in range(len(in_text[i])):
            if in_text[i][j] == " ":
                res_str += " "
            elif in_text[i][j] != " " and in_text[i][j - 1] == " ":
                res_str += str_list_end[i][k]
                k += 1
        if in_text[i][0] != " " and res_str[0] == " ":
            res_str = res_str[1:]
        print(res_str)
    print()


def max_word_input(in_text):
    len_word = int(input("Введите необходимую длину слова: "))
    print()
    str_list_wordcnt = []
    text_str = "".join(in_text)
    sen_list = text_str.split(".")
    for sen in sen_list:
        str_list = sen.split()
        k = 0
        for word in str_list:
            if len(word.strip(",")) == len_word:
                k += 1
        str_list_wordcnt.append(k)
    maximum_len = max(str_list_wordcnt)
    for i in range(len(str_list_wordcnt)):
        if str_list_wordcnt[i] == maximum_len:
            print(sen_list[i] + ".\n")


def max_word_digit(in_text):
    digit = input("Введите необходимую букву: ")
    print()
    str_list_wordcnt = []
    text_str = "".join(in_text)
    sen_list = text_str.split(".")
    for sen in sen_list:
        str_list = sen.split()
        k = 0
        for word in str_list:
            if digit in word:
                k += 1
        str_list_wordcnt.append(k)
    maximum_in = max(str_list_wordcnt)
    for i in range(len(str_list_wordcnt)):
        if str_list_wordcnt[i] == maximum_in:
            print(sen_list[i] + ".\n")


def max_word_replacer(in_text):
    str_list_wordcnt = []
    str_list_end = []
    text_str = " ".join(in_text)
    sen_list = text_str.split(".")
    for sen in sen_list:
        str_list = sen.split()
        str_list_end.append(str_list)
        str_list_wordcnt.append(len(str_list))
    local_max = str_list_wordcnt[0]
    for x in str_list_wordcnt:
        if x > local_max:
            local_max = x
    max_word_sen = str_list_end[str_list_wordcnt.index(local_max)]
    max_word_ind = str_list_wordcnt.index(local_max)
    max_len = len(max_word_sen[0])
    needed_word = max_word_sen[0]
    for word in max_word_sen:
        if len(word) > max_len:
            needed_word = word
            max_len = len(word)
    sen_list[max_word_ind] = sen_list[max_word_ind].replace(needed_word, "")
    print(sen_list[max_word_ind] + ".")
    print()

while True:
    
    result = menu_title()

    if result == 1:
        weight_alignment(text_preparation(input_text))
    elif result == 2:
        left_edge_alignment(text_preparation(input_text))
    elif result == 3:
        right_edge_alignment(text_preparation(input_text))
    elif result == 4:
        replacer(input_text)
    elif result == 5:
        deleter(input_text)
    elif result == 6:
        evaler(input_text)
    elif result == 7:
        max_word_input(input_text)
    elif result == 8:
        max_word_digit(input_text)
    elif result == 9:
        max_word_replacer(input_text)
    elif result == 0:
        break
