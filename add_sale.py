import json
import sys

#   для записи данных и для вывода на экран записанных данных.
#   При записи передавать из командной строки значение суммы продаж.
#   Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.

#rezult_for_add = input()
program, *args = sys.argv

#print()
#print('считываем файл sales.json')

try:
    with open('bakery.csv', 'r', encoding='utf-8') as file_in:
        rezult = file_in.readlines()
except FileNotFoundError:
    rezult = []
    rezult.append('\n')


for arg in args:
    rezult.append(arg + '\n')

#print('Перезаписываем результат в файл sales.json')
with open('bakery.csv', 'w', encoding='utf-8') as file_sales:
    file_sales.writelines(rezult)

print('Запись добавлена')