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
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов
#


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# if __name__ == '__main__':
#     print_hi('PyCharm')
