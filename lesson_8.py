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


import re

def email_parse(text):
    email_pattern = re.compile(r'^[A-Za-z0-9\._-]+@[A-Za-z0-9\._-]+')
    email_pattern1 = re.compile(r'^[A-Za-z0-9\._-]+@')
    email_pattern3 = re.compile(r'@*[A-Za-z0-9_-]*\.[A-Za-z]+')
    email_pattern4 = re.compile(r'[^@[^@]+\.[^@]+')

    temp = email_pattern.match(text)
    temp1 = email_pattern1.match(text)

    temp3 = email_pattern3.search(text)
    temp4 = email_pattern4.match(text)

    return email_pattern.match(text)



email_parse('someone@geekbrains.ru')


# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)

# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)





# 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5