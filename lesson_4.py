
# 1. Проверить, установлен ли пакет pillow в глобальном окружении.
#  Если да — зафиксировать версию.
#  Установить самую свежую версию pillow, если ранее она не была установлена.
#  Сделать подтверждающий скриншот. Создать и активировать виртуальное окружение.
#  Убедиться, что в нем нет пакета pillow. Сделать подтверждающий скриншот.
#  Установить в виртуальное окружение pillow версии 7.1.1 (или другой, отличной от самой свежей).
#  Сделать подтверждающий скриншот.
#  Деактивировать виртуальное окружение.
#  Сделать подтверждающий скриншот.
#  Скрины нумеровать двухразрядными числами, например: «01.jpg», «02.jpg».
#  Если будут проблемы с pillow - можно поработать с другим пакетом: например, requests.


# ГЛОБАЛЬНОЕ ОКРУЖЕНИЕ

# узнать версию пакета
# C:\> pip show pillow
# WARNING: Package(s) not found: pillow
# C:\> pip install pillow
# Successfully installed pillow-9.1.0
# C:\> pip show pillow
# Name: Pillow
# Version: 9.1.0


# ЛОКАЛЬНОЕ ОКРУЖЕНИЕ

# Чтобы начать пользоваться виртуальным окружением, необходимо его активировать:
# venv\Scripts\activate.bat - для Windows;
# source venv/bin/activate - для Linux и MacOS.
# Справолчно: source выполняет bash-скрипт без запуска дополнительного bash-процесса.
# Проверить успешность активации можно по приглашению оболочки (venv). Она будет выглядеть так:
# (venv) root@purplegate:/var/test#

# C:\Users\PKV90>cd C:\repository github\GB_PY_0001\venv\Scripts
# C:\repository github\GB_PY_0001\venv\Scripts>activate
# (venv) C:\repository github\GB_PY_0001\venv\Scripts>pip show pillow
# WARNING: Package(s) not found: pillow
# (venv) C:\repository github\GB_PY_0001\venv\Scripts>pip install pillow==9.0.0
# Collecting pillow==9.0.0
#   Downloading Pillow-9.0.0-cp310-cp310-win_amd64.whl (3.2 MB)
#      ---------------------------------------- 3.2/3.2 MB 6.0 MB/s eta 0:00:00
# Installing collected packages: pillow
# Successfully installed pillow-9.0.0
#
# (venv) C:\repository github\GB_PY_0001\venv\Scripts>pip show pillow
# Name: Pillow
# Version: 9.0.0
# (venv) C:\repository github\GB_PY_0001\venv\Scripts>deactivate.bat
# C:\repository github\GB_PY_0001\venv\Scripts>cd /
# C:\>pip show pillow
# Name: Pillow
# Version: 9.1.0

# 2. Написать функцию currency_rates(),
# принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.

import requests

def currency_rates(currency_name):
    url = 'http: // www.cbr.ru / scripts / XML_daily.asp'
    response = requests.get(url, verify=False)
    print(response.status_code)
    temp_json = response.json()
    print(temp_json)
    pass

currency_rates('USD')



# 4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.


