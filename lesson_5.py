# 1. Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...

print()
print('Задание 1')
print('________________________________________________________')
print()


# nums_gen_15 = (num for num in range(1, 15 + 1, 2))
# print(*nums_gen_15)


def odd_nums(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


odd_to_15 = odd_nums(15)

print(type(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(*odd_to_15)

# 3. Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]

# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
#
# ### Доказать, что вы создали именно генератор.
# Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.

print()
print('Задание 3')
print('________________________________________________________')
print()

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen = (
    (tutors_item, klasses_item) for tutors_item, klasses_item in zip(tutors, klasses)
    if tutors_item
)
print('Type generator:', type(gen))
# print('Type item:', type(next(gen)))

print()
print(next(gen))
print(next(gen))
print(next(gen))
for a in gen:
    print(a)

print()
print('Если в списке klasses меньше элементов, чем в списке tutors - вариант 1')
print('Много строк: используем ловим исключение StopIteration и пост-обработка')
print()

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б']

gen_tutors = (tutors_item for tutors_item in tutors)
gen_klasses = (klasses_item for klasses_item in klasses)


def get_item(gen):
    try:
        next_item = next(gen)
        return next_item
    except StopIteration:
        return None


print((get_item(gen_tutors), get_item(gen_klasses)))
print((get_item(gen_tutors), get_item(gen_klasses)))
print((get_item(gen_tutors), get_item(gen_klasses)))
print((get_item(gen_tutors), get_item(gen_klasses)))
print((get_item(gen_tutors), get_item(gen_klasses)))
print((get_item(gen_tutors), get_item(gen_klasses)))

print()
print('Если в списке klasses меньше элементов, чем в списке tutors - вариант 2')
print('Меньше строк: используем itertools(zip_longest), так как zip ограничивается по меньшей последовательности ')
print()

from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б']

gen_var_2 = (
    (tutors_item, klasses_item) for tutors_item, klasses_item in zip_longest(tutors, klasses)
)

print('Type generator:', type(gen_var_2))
print()

for i in gen_var_2:
    print(i)

# ### 4. Представлен список чисел.
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55
# Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# result = [12, 44, 4, 10, 78, 123]
# ```

# Подсказка: использовать возможности python, изученные на уроке.


print()
print('Задание 4')
print('________________________________________________________')
print()

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

gen_src_6 = [b for a, b in zip(src, src[1:]) if b > a]
print(gen_src_6)

# 5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке,
# например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

print()
print('Задание 5')
print('________________________________________________________')
print()

import sys
from time import perf_counter

print('Исходная последовательность')
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(src)
print()

print('------решение в лоб----------')
start = perf_counter()
unique_src_initial_order = [item for item in src if src.count(item) == 1]
print('result')
print(unique_src_initial_order)
print('Size', sys.getsizeof(src))
print('Time', perf_counter() - start)
print()

print('------оптимизируем----------')

start = perf_counter()

src_unique = set(src)

src_unique_dict = {}
for item in src:
    if item in src_unique_dict.keys():
        src_unique_dict[item] += 1
    else:
        src_unique_dict[item] = 1

result = [key for key in src if src_unique_dict[key] == 1]
print('result')
print(result)

print('Size', sys.getsizeof(result))
print('Time', perf_counter() - start)

print()
print('------оптимизируем----------')

start = perf_counter()

src_unique = set()
src_not_unique = set()

for item in src:
    if item in src_unique:
        src_not_unique.add(item)
    else:
        src_unique.add(item)

result = [key for key in src if key not in src_not_unique]
print('result')
print(result)

print('Size', sys.getsizeof(result))
print('Time', perf_counter() - start)
