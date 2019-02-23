"""" Выполнение действий над набором записей, хранящемся в файле.

Данная программа позволяет проделать над записями в файле такие
операции, как: выбор файла, создание в файле нового набора записей
добавление записей к уже существующим, вывод всех записей, поиск
среди записей по одному полю, поиск среди записей по двум полям.
Каждая запись в файле хранится в одной строке, разделитель полей
записи - пробел.
"""


def menu_title():
    """ Вызов меню. Функция позволяет пользователю выбрать операцию
    из списка для выполнения выбранной над файлом.

    Входные/выходные данные:

    menu_number - выбранный номер из меню (возвращается в случае
    выполнения функции без ошибок) """
    while True:
        print("*"*38)
        print("  Выберите действие:\n"
              "1. Выбрать файл\n"
              "2. Создать в файле новый набор записей\n"
              "3. Добавить записи\n"
              "4. Вывести все записи\n"
              "5. Поиск по одному полю\n"
              "6. Поиск по двум полям\n"
              "\n"
              "0. Выход")
        print("*"*38)

        try:
            menu_number = int(input("Введите номер операции: "))
            print()

            if menu_number > 6 or menu_number < 0:
                print("Операции с данным номером не существует!\n")
            else:
                return menu_number

        except ValueError:
            print("Введены некорректные данные\n")


def choose_file():
    """ Выбор файла (из директории, в которой находится
    исходный код.

    Входные/выходные данные:

    file_name - имя выбираемого файла

    Промежуточные значения:

    file_used - привязка файла к переменной """
    while True:
        try:
            file_name = input("Введите имя файла: ")
            file_used = open(file_name)
            file_used.close()
            print()

            return file_name

        except IOError:
            print("Файла по Вашему запросу не найдено, "
                  "проверьте введенные данные!")


def create_record(in_file):
    """ Создание в файле нового набора записей. Функция полностью
    перезаписывает содержимое файла, оставляя только те записи, которые
    будут добавлены при вызове этой функции.

    Входные данные:

    in_file - файл, в который будет производиться запись
    record_num - количество записей для записи
    temp_record - очередная запись для записи

    Промежуточные значения:

    file_used - привязка файла к переменной
    temp_record_list - список записей для единовременной записи в конце
    ввода """
    if in_file is not None:
        file_used = open(in_file, "w")
        print("Работа с файлом {}:".format(in_file))
        record_num = int(input("Введите количество новых записей: "))
        temp_record_list = []
        for i in range(record_num):
            print("Введите запись {0} для записи в файл: ".format(i+1))
            temp_record = input()
            temp_record += "\n"
            temp_record_list.append(temp_record)
        file_used.writelines(temp_record_list)
        file_used.close()
        
    else:
        print("Файл не выбран. Выберите файл!")
    print()


def add_record(in_file):
    """ Добавление нового набора записей в файл. Функция добавляет
    к уже имеющимся записям новые, которые будут введены пользователем.

    Входные данные:

    in_file - файл, в который будет производиться запись
    record_num - количество записей для записи
    temp_record - очередная запись для записи

    Промежуточные значения:

    file_used - привязка файла к переменной
    temp_record_list - список записей для единовременной записи в конце
    ввода """
    if in_file is not None:
        file_used = open(in_file, "a+")
        print("Работа с файлом {}:".format(in_file))
        record_num = int(input("Введите количество новых записей: "))
        temp_record_list = []
        for i in range(record_num):
            print("Введите запись {0} для записи в файл: ".format(i+1))
            temp_record = input()
            temp_record += "\n"
            temp_record_list.append(temp_record)
        file_used.writelines(temp_record_list)
        file_used.close()

    else:
        print("Файл не выбран. Выберите файл!")
    print()


def output_all_records(in_file):
    """ Вывод всех записей из файла в консоль.

    Входные данные:

    in_file - файл, в который будет производиться запись

    Промежуточные значения:

    file_used - привязка файла к переменной
    line - единичная запись в файле """
    if in_file is not None:
        file_used = open(in_file)
        print("Работа с файлом {}:".format(in_file))
        for line in file_used:
            print(line, end="")
    else:
        print("Файл не выбран. Выберите файл!")
    print()


def one_field_search(in_file):
    """ Поиск среди записей по одному заданному полю. Функция
    по заданному полю выводит все записи, в которых введенное
    пользователем поле совпадает с таковым в записи.

    Входные данные:

    in_file - файл, в который будет производиться запись
    needed_field - поле, по которому производится поиск

    Промежуточные значения:

    records_list - список записей, в котором хранятся записи
    в виде списков полей
    line_list - список полей записи
    line - единичная запись в файле

    Выходные данные:

    res_str - записи, удовлетворяющие поиску """
    if in_file is not None:
        file_used = open(in_file)
        print("Работа с файлом {}:".format(in_file))
        records_list = []
        needed_field = input("Введите поле, по которому необходимо"
                             " произвести поиск: ")
        print()

        res_str = None
        
        for line in file_used:
            line_list = line.split()
            records_list.append(line_list)
        for x in records_list:
            if needed_field in x:
                res_str = " ".join(x)
                print(res_str)
        if res_str is None:
            print("Записей с данными параметрами не найдено!")
            
    else:
        print("Файл не выбран. Выберите файл!")
    print()


def two_field_search(in_file):
    """ Поиск среди записей по двум заданным полям. Функция
    по заданным полям выводит все записи, в которых введенные
    пользователем поля совпадают с таковыми в записи.

    Входные данные:

    in_file - файл, в который будет производиться запись
    needed_field_one - первое поле, по которому производится поиск
    needed_field_two - второе поле, по которому производится поиск

    Промежуточные значения:

    records_list - список записей, в котором хранятся записи
    в виде списков полей
    line_list - список полей записи
    line - единичная запись в файле

    Выходные данные:

    res_str - записи, удовлетворяющие поиску """
    if in_file is not None:
        file_used = open(in_file)
        print("Работа с файлом {}:".format(in_file))
        records_list = []
        needed_field_one = input("Введите первое поле, по которому необходимо"
                                 " произвести поиск: ")
        needed_field_two = input("Введите второе поле, по которому необходимо"
                                 " произвести поиск: ")
        print()

        res_str = None
        
        for line in file_used:
            line_list = line.split()
            records_list.append(line_list)
        for x in records_list:
            if needed_field_one in x and needed_field_two in x:
                res_str = " ".join(x)
                print(res_str)
        if res_str is None:
            print("Записей с данными параметрами не найдено!")
        
    else:
        print("Файл не выбран. Выберите файл!")
    print()

    
input_file = None

while True:
    
    result = menu_title()

    if result == 1:
        input_file = choose_file()
    elif result == 2:
        create_record(input_file)
    elif result == 3:
        add_record(input_file)
    elif result == 4:
        output_all_records(input_file)
    elif result == 5:
        one_field_search(input_file)
    elif result == 6:
        two_field_search(input_file)
    elif result == 0:
        break
