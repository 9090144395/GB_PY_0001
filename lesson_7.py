# 1. Написать скрипт, создающий стартер (заготовку) для проекта
# со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание:
# подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# Ответ: либо использовать обработчик ошибок либо использовать os.path.exists
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять
# имена папок под конкретный проект;
# Ответ: я бы предпочел отдельный файл, но можно сделать и через диалог
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках
# и файлах (добавлять детали)?
# Ответ: расширять можно при использовании отдельного файла для настроек.

print()
print('Задание 1')
print('________________________________________________________')
print()

import os

list_subroot = [
    '--settings',
    '--mainapp',
    '--adminapp',
    '--authapp'
]

current_dir = os.path.abspath('.')

for subdir in list_subroot:
    dir_path = os.path.join(current_dir, subdir)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        print('Done -> ', dir_path)

# 3. Создать структуру файлов и папок, как написано в задании 2
# (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание:
# исходные файлы необходимо оставить;
# обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.

print()
print('Задание 3')
print('________________________________________________________')
print()

import os
import yaml
from shutil import copyfile, copy, copy2

yaml_text = '''
---
- settings:
  - __init__.py
  - dev.py
  - prod.py
- mainapp:
  - __init__.py
  - models.py
  - views.py
- mainapp\\templates\\mainapp:
  - base.html
  - index.html
- authapp:
   - __init__.py
   - models.py
   - views.py
- authapp\\templates\\authapp:
  - base.html
  - index.html
'''

yaml_format = yaml.safe_load(yaml_text)

print('Создаем исходную структуру папок скриптом на базе yaml')
for dict_in_yaml in yaml_format:
    for dir, files in dict_in_yaml.items():
        for file in files:
            if not os.path.exists(dir):
                os.makedirs(dir)
            file_path = os.path.join(dir, file)
            with open(file_path, 'w') as f:
                f.write('')

print()
current_dir = os.path.abspath('.')
if not os.path.exists('templates'):
    os.mkdir('templates')
path_target = '.\\templates'

print('Сканируем существующие папки')
for root, dirs, files in os.walk('.'):
    if 'templates' in root.lower() and not root.lower().startswith('.\\templates'):
        for file in files:
            target_folder = root.split('\\')[-1]
            path_target_new = os.path.join('.\\templates', target_folder)

            if not os.path.exists(path_target_new):
                print('Создаем папку', path_target_new)
                os.mkdir(path_target_new)

            source_file = os.path.join(root, file)
            if not os.path.exists(os.path.join(path_target_new, source_file)):
                print('Копируем файл', source_file, ' в ', path_target_new)
                copy2(source_file, path_target_new)

# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

print()
print('Задание 4')
print('________________________________________________________')
print()

from collections import defaultdict

folder_for_stats = '.'
dict_result = defaultdict(int)
for root, dirs, files in os.walk('.'):
    if root.startswith(folder_for_stats):
        for file in files:
            file_size = os.stat(os.path.join(root, file)).st_size
            file_size_round = round(file_size, 0)
            #print(file_size_round)

            gen = (10**item for item in range(0, 100))
            for i in gen:
                if file_size_round >= i and file_size_round < i*10:
                    dict_result[i] += 1
                    break
                elif file_size_round == 0:
                    dict_result[0] += 1
                    break



print(sorted(dict_result.items()))
print(dict_result)