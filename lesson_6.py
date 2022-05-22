# 1. Не используя библиотеки для парсинга,
# распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
#
# Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

print()
print('Задание 1')
print('________________________________________________________')
print()

import requests
import sys

print('Делаем запрос на сервер...')
url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = requests.get(url, verify=None)
print('Response.status_code', response.status_code)
print('Size response', sys.getsizeof(response.text))

# сохраняем ответ в файл
with open('response.txt', 'w', encoding='utf-8') as file:
    file.write(response.text)
print('Ответ запроса записан в файл response.txt')
print('')

target_list =[]
with open('response.txt', 'r', encoding='utf-8') as file:
    # читаем по строкам на случай очень большого файла
    line = file.readline()
    while line:
        #print(line)
        split_line = line.split()
        target_list.append((split_line[0],split_line[5][1:],split_line[6]))
        line = file.readline()

print('Выводим на экран первые три элемента результирующего списка: ')
print(target_list[0])
print(target_list[1])
print(target_list[2])



# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип:
# одна строка — один пользователь, разделитель между значениями — запятая.

# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл.
# Проверить сохранённые данные.

# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
# задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1».
#
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
#
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи

print()
print('Задание 3')
print('________________________________________________________')
print()

# Исходные данные для задачи hobby.csv и users.csv:
# сохраняем ответ в файл

temp_1 = [
    'Иванов,Иван,Иванович',
    '\n',
    'Петров,Петр,Петрович',
    '\n',
    'Сидоров,Марк,Петрович',
    '\n'
]
with open('users.csv', 'w', encoding='utf-8') as file:
    file.writelines(temp_1)

temp_2 = [
    'скалолазание,охота',
    '\n',
    'горные лыжи',
    '\n',
]
with open('hobby.csv', 'w', encoding='utf-8') as file:
    file.writelines(temp_2)

# ----------------

from itertools import zip_longest
import json

with open('users.csv', 'r', encoding='utf-8') as file_users:
    with open('hobby.csv', 'r', encoding='utf-8') as file_hobby:
        lines_users = file_users.readlines()
        lines_hobby = file_hobby.readlines()
        count_users = len(lines_users)
        count_hobby = len(lines_hobby)

        print('Количество строк в file_users:', count_users)
        print('Количество строк в file_hobby:', count_hobby)

        # Если в файле, хранящем данные о ФИО, меньше записей, чем в файле с хобби,
        # выходим из скрипта с кодом «1».

        if count_users < count_hobby:
            exit(1)

        # Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
        # задаём в словаре значение None.

        gen = zip_longest(lines_users,lines_hobby)
        rezult = {}
        for user, hobby in gen:
            rezult[str(user).replace('\n','').replace(',',' ')] = str(hobby).replace('\n','')

        print(rezult)

        # записываем в файл (сериализация)
        print('Записываем результат в файл rezult.json')
        with open('rezult.json', 'w', encoding='utf-8') as file_out:
            json.dump(rezult, file_out)

        # проверяем, считываем файл (десериализация)
        print()
        print('Проверка - считываем записанный файл rezult.json')
        with open('rezult.json', 'r', encoding='utf-8') as file_in:
            read_from_file_json = json.load(file_in)
            print(read_from_file_json)

        # gen = [(user,hobby) for user,hobby in result]
        # print(gen)

        # записать код, загружающий данные из обоих файлов и формирующий из них словарь:
        # ключи — ФИО, значения — данные о хобби.
        # Сохранить словарь в файл.
        # Проверить сохранённые данные.




# 6. Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки:
#   для записи данных и для вывода на экран записанных данных.
#   При записи передавать из командной строки значение суммы продаж.
#
# Для чтения данных реализовать в командной строке следующую логику:
#   просто запуск скрипта — выводить все записи;
#   запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
#   запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
#
# Примеры запуска скриптов:
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1
