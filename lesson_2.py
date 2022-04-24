'''
1. Выяснить тип результата выражений:
15 * 3
15 / 3
15 // 2
15 ** 2
'''

print()
print('Задание 1')
print('________________________________________________________')
print()

print('(15 * 3) type - ', type(15 * 3))
print('(15 / 3) type - ', type(15 / 3))
print('(15 // 2) type - ', type(15 // 2))
print('(15 ** 2) type - ', type(15 ** 2))

'''
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками 
(добавить кавычку до и кавычку после элемента списка, являющегося числом) 
и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? 
Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. 
Главное: дополнить числа до двух разрядов нулём!
'''

print()
print('Задание 2')
print('________________________________________________________')
print()

default_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []  # тут будет обработанный список
for item in default_list:
    # print(type(item))
    if item.isnumeric():
        new_list.append('"')
        if len(item) == 1:
            new_list.append('0' + item)
        else:
            new_list.append(item)
        new_list.append('"')
    elif item[:1] == '+':
        if item[1:].isnumeric():
            new_list.append('"')
            if len(item[1:]) == 1:
                new_list.append('+' + '0' + item[1:])
            else:
                new_list.append('+' + item[1:])
            new_list.append('"')
    elif item[:1] == '-':
        if item[1:].isnumeric():
            new_list.append('"')
            if len(item[1:]) == 1:
                new_list.append('-' + '0' + item[1:])
            else:
                new_list.append('-' + item[1:])
            new_list.append('"')
    else:
        new_list.append(item)

print(new_list)

new_list_for_print = []  # тут будет список для вывода в виде предложения
for item in new_list:
    if item.isnumeric():
        new_list_for_print.pop()
        new_list_for_print.append(item)
    elif item[1:].isnumeric():
        new_list_for_print.pop()
        new_list_for_print.append(item)
    else:
        new_list_for_print.append(item)
        new_list_for_print.append(' ')

# print(new_list_for_print)
# print(*new_list_for_print)
print(''.join(new_list_for_print))

'''
4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки. 
Сформировать и вывести на экран фразы вида: 'Привет, Игорь!' 
Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. 
Можно ли при этом не создавать новый список?
'''

print()
print('Задание 3')
print('________________________________________________________')
print()

input_list = [
    'инженер-конструктор Игорь',
    'главный бухгалтер МАРИНА',
    'токарь высшего разряда нИКОЛАй',
    'директор аэлита'
]

for words in input_list:
    print('Привет, ', words.split()[-1].title(), '!', sep='')

print()
print('Можно ли при этом не создавать новый список?')
print('Да - путем поиска последнего пробела, но использование split выглядит более элегантным решением :) ')

'''
5. Создать список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, 
цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). 
Подумать, как из цены получить рубли и копейки, как добавить нули, если, 
например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

Вывести цены, отсортированные по возрастанию, новый список не создавать 
(доказать, что объект списка после сортировки остался тот же).

Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. 
Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
'''

print()
print('Задание 4')
print('________________________________________________________')
print()

list_for_price = [
    57.8,
    46.51,
    97,
    4.6,
    5.7,
    6.8,
    7.9,
    8.1,
    9.2,
    10.1
]

print(*list_for_price, sep=', ')
print()
print('Вариант работы с текстом (переводим в текст, пилим сплитом по точке в список и далее работаем с ним)')
for item in list_for_price:
    item_for_print_list = str(item).split('.')
    if len(item_for_print_list) == 2:
        print(item_for_print_list[0], ' руб', sep='', end=' ')
        print(item_for_print_list[1], ' коп', sep='', end=', ')

    elif len(item_for_print_list) == 1:
        print(item_for_print_list[0], ' руб', sep='', end=', ')

print()
print()
print('Добавляем нули (7 коп -> 07 коп)')

for item in list_for_price:
    item_for_print_list = str(item).split('.')
    if len(item_for_print_list) == 2:
        print(item_for_print_list[0], ' руб', sep='', end=' ')
        if len(item_for_print_list[1]) == 1:
            print('0', item_for_print_list[1], ' коп', sep='', end=', ')
        else:
            print(item_for_print_list[1], ' коп', sep='', end=', ')

    elif len(item_for_print_list) == 1:
        print(item_for_print_list[0], ' руб', sep='', end=', ')

print()
print()
print('Вариант работы с числом (целая часть и остаток от целочисленного деления на 1)')

# print(list_for_price)
# list_for_price.sort()

print('Исходный список')
print(*list_for_price, sep=', ')
print()

print('Выводим в сортированном виде по возрастанию')

for item in sorted(list_for_price):
    item_integer = round(item // 1)
    item_fractional = round(item % 1,2)

    print(item_integer, ' руб', sep='', end='')
    if item_fractional != 0:
        print(' ' , str(item_fractional)[2:], ' коп', sep='', end='')

    print(', ', sep='', end='')

print()
print()
print('Проверяем исходный список после вывода сортированного')
print(*list_for_price, sep=', ')

print()
print('Создать новый список, содержащий те же цены, но отсортированные по убыванию.')
sort_list_for_price = sorted(list_for_price, reverse=True)
print(*sort_list_for_price, sep=', ')


print()
print('Вывести цены пяти самых дорогих товаров')
print(*sort_list_for_price[:5], sep=', ')


