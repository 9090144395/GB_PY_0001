#Для чтения данных реализовать в командной строке следующую логику:
#   просто запуск скрипта — выводить все записи;
#   запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
#   запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму числу, включительно.


import json
import sys

program, *args = sys.argv

#print()
#print('считываем файл sales.json')

try:
    with open('bakery.csv', 'r', encoding='utf-8') as file_in:
        rezult = file_in.readlines()
except FileNotFoundError:
    rezult = []
    rezult.append('\n')

if len(args) == 0:
    print(*rezult)
elif len(args) == 1:
    start = int(args[0])
    print(*rezult[start:])
elif len(args) == 2:
    start = int(args[0])
    stop = int(args[1]) + 1
    print(*rezult[start:stop])

