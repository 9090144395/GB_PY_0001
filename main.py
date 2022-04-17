### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек
# Примечание: можете проверить себя здесь, подумайте, можно ли использовать цикл для проверки работы кода сразу для нескольких значений продолжительности, будет ли тут полезен список?

print()
print('Задание 1')
print('________________________________________________________')
print()

input_string = input('Введите длительность в секундах: ')
print(f'Получено значение -> {input_string}')
is_int = input_string.isnumeric()
# если число
if is_int:
    input_sec = int(input_string)
    # если меньше минуты
    if input_sec > 0 and input_sec < 60:
        print(f'{input_sec} сек')
    # если больше минуты но меньше часа
    elif input_sec >= 60 and input_sec < 3600:
        input_minute = input_sec // 60
        remains_sec = input_sec % 60
        print(f'{input_minute} мин {remains_sec} сек')
    # если больше часа но меньше дня
    elif input_sec >= 3600 and input_sec < 86400:
        input_minute = input_sec // 60
        remains_sec = input_sec % 60
        input_hours = input_minute // 60
        remains_minute = input_minute % 60
        print(f'{input_hours} час {remains_minute} мин {remains_sec} сек')
    # если обльше дня
    elif input_sec >= 86400:
        input_minute = input_sec // 60
        remains_sec = input_sec % 60
        input_hours = input_minute // 60
        remains_minute = input_minute % 60
        input_day = input_hours // 24
        remains_hours = input_hours % 24
        print(f'{input_day} день {remains_hours} час {remains_minute} мин {remains_sec} сек')
    # другие случаи
    else:
        print('Что-то пошло не так :( ')
else:
    print('Введенное занчение не является целым числом или отрицательное')

# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

print()
print('Задание 2')
print('________________________________________________________')
print()

target_list = []
target_summa = 0
for item_in_range in range(1, 100, 2):
    target_list.append(pow(item_in_range, 3))

print('Список, состоящий из кубов нечётных чисел от 1 до 1000:')
print(target_list)

for item_in_list in target_list:
    print()
    print('Разбор цифр', item_in_list)
    count_1000000 = item_in_list // 1000000
    remains_from_1000000 = item_in_list % 1000000
    count_100000 = remains_from_1000000 // 100000
    remains_from_100000 = item_in_list % 100000
    count_10000 = remains_from_100000 // 10000
    remains_from_10000 = item_in_list % 10000
    count_1000 = remains_from_10000 // 1000
    remains_from_1000 = item_in_list % 1000
    count_100 = remains_from_1000 // 100
    remains_from_100 = item_in_list % 100
    count_10 = remains_from_100 // 10
    remains_from_10 = item_in_list % 10
    count_1 = remains_from_10

    print(count_1000000)
    print(count_100000)
    print(count_10000)
    print(count_1000)
    print(count_100)
    print(count_10)
    print(count_1)

    summa = (
            count_1
            + count_10
            + count_100
            + count_1000
            + count_10000
            + count_100000
            + count_1000000
    )

    print(summa)
    if summa % 7 == 0:
        print('Сумма цифр числа = ', summa, '(делится на 7 без остатка)')
        print('--> Включаем число в итоговую сумму:',
              target_summa,
              ' + ',
              item_in_list,
              ' = ',
              target_summa + item_in_list)
        target_summa += item_in_list
    else:
        print('Сумма цифр числа = ', summa, '(НЕ делится на 7 без остатка)')

print('Итоговая сумма', target_summa)

# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов
#
print()
print('Задание 3')
print('________________________________________________________')
print()

last_number_in_input_proc = None
for item in range(1, 101):

    if item < 10:
        last_number_in_input_proc = item
    elif item >= 10 and item <= 99:
        last_number_in_input_proc = item % 10
    elif item == 100:
        last_number_in_input_proc = 0
    elif item > 100:
        print('Логика скрипта не предусматривает более 100 процентов')

    if last_number_in_input_proc == 1:
        print(f'{item} процент')
    elif last_number_in_input_proc in [2, 3, 4]:
        print(f'{item} процента')
    else:
        print(f'{item} процентов')
    pass

print('Готово')
