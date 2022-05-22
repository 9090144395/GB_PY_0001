import json
import sys

#rezult_for_add = input()

program, *args = sys.argv


print()
print('считываем записанный файл sales.json')

try:
    with open('sales.json', 'r', encoding='utf-8') as file_in:
        rezult = json.load(file_in)
except FileNotFoundError:
    rezult = []

rezult.append(args)


print('Перезаписываем результат в файл sales.json')
with open('sales.json', 'w', encoding='utf-8') as file_sales:
    json.dump(rezult, file_sales)