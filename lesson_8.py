# 1. Написать функцию email_parse(<email_address>),
# которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса
# и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError.
#
# Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть
# их в регулярном выражении; имеет ли смысл в данном случае использовать функцию re.compile()?

print()
print('Задание 1')
print('________________________________________________________')
print()

import re

def email_parse(text):

    email_pattern = re.compile(r'^[A-Za-z0-9\._-]+@')
    domen_pattern = re.compile(r'@[A-Za-z0-9_-]+\.[A-Za-z]{2,3}')

    username = email_pattern.match(text)
    domain = domen_pattern.search(text)
    assert email_pattern.match(text), f'ValueError {text}'

    return {'username': username[0][:-1], 'domain': domain[0][1:]}


print('someone@geekbrains.ru')
print(email_parse('someone@geekbrains.ru'))
print('some_4.one-1980@geekbrains.com')
print(email_parse('some_4.one-1980@geekbrains.com'))
#print(email_parse('someone@geekbrains.c')) # для проверки исключения
#print(email_parse('someonegeekbrains.ru')) # для проверки исключения


# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? да
# Сможете ли решить задачу для именованных аргументов? да
# Сможете ли вы замаскировать работу декоратора? затрудняюсь ответить... использовать специальный декоратор wraps из модуля functools?
# Сможете ли вывести имя функции, например, в виде: да
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

print()
print('Задание 3')
print('________________________________________________________')
print()

def type_logger(func):
    cache = {}

    def wrapper(*args):
        nonlocal cache

        for arg in args:
            key = func(arg)
            args_type = type(arg)
            if key not in cache:
                cache[key] = args_type

        #return f'{key} : {args_type}'
        return cache.items()
    return wrapper


@type_logger
def calc_cube(x):
   return x ** 3


print(calc_cube(5))
print(calc_cube(4,8))
print(calc_cube(3))



# 4. Написать декоратор с аргументом-функцией (callback),
# позволяющий валидировать входные значения функции и выбрасывать исключение ValueError,
# если что-то не так, например:
# def val_checker...
#     ...
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5

# Примечание: сможете ли вы замаскировать работу декоратора?
# да, использовать специальный декоратор wraps из модуля functools

print()
print('Задание 4')
print('________________________________________________________')
print()
def val_checker(arg_decorator):
    def _val_checker(func):
        def wrapper(*args):
            for arg in args:
                validate = arg_decorator(arg)
                if validate:
                    key = func(arg)
                else:
                    raise ValueError('Ups...ValueError: wrong val ')
            return key

        return wrapper
    return _val_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

print('calc_cube(5)')
print(calc_cube(5))
print('calc_cube(-5) ... для вызова исключения')
print(calc_cube(-5))

# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5