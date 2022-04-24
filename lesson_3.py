'''
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
'''

print()
print('Задание 1')
print('________________________________________________________')
print()

print()
print('Вариант через for:')


def num_translate(word):
    list_eng = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    list_rus = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    list_final = []
    for item_eng, item_rus in zip(list_eng, list_rus):
        if item_eng == word:
            return print(item_rus)
    return None


num_translate('one')
num_translate('eight')
num_translate('sgtrbggdt')

print()
print('Вариант через filter:')


def num_translate(word):
    list_eng = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    list_rus = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    list_final = list(zip(list_eng, list_rus))

    # print(list_final[0])

    def simple(x):
        temp_ = x[0]
        if x[0] == word:
            return True
        else:
            return False

    temp = filter(simple, list_final)  # в результате имеем одноразовый итератор (еще не список)
    out_list = list(temp)  # а тут превращаем в список

    if len(out_list) == 0:
        return None
    else:
        return print(out_list[0][1])


num_translate('one')
num_translate('eight')
num_translate('sgtrbggdt')

'''
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, 
в котором ключи — первые буквы имён, 
а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. 

Например:
thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Да, для функции 
Как поступить, если потребуется сортировка по ключам? sorted(out_dict, key=out_dict.get)
Можно ли использовать словарь в этом случае? затрудняюсь с ответов
'''

print()
print('Задание 3')
print('________________________________________________________')
print()


def thesaurus(*args):
    '''
    Функция по задаче 3
    '''
    input_list = args
    # print(input_list)
    first_letter = set(list(map(lambda x: x[0], input_list)))
    # print(first_letter)

    out_dict = {}
    for item in first_letter:
        # print(item)
        out_name = list(filter(lambda x: x.startswith(item), input_list))
        # print(out_name)
        out_dict[item] = out_name

    print('Словарь:')
    print(out_dict)

    print('Сортированный словарь:')
    sorted_keys = sorted(out_dict, key=out_dict.get)
    sorted_dict = {}
    for w in sorted_keys:
        sorted_dict[w] = out_dict[w]
    print(sorted_dict)

    return None


thesaurus("Иван", "Мария", "Петр", "Илья")

# print(help(thesaurus))

'''
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, 
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках 
(когда каждое слово можно использовать только в одной шутке)? 
Сможете ли вы сделать аргументы именованными?
'''



print()
print('Задание 5')
print('________________________________________________________')
print()

from random import randrange
from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(count):
    '''
    Возвращает шутки, созданные случайным образом из трех списков со словами
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    :param count: количество шуток
    :return: None
    '''

    i_count = 1
    while i_count <= count:
        random_idx = randrange(len(nouns)) # не лучший вариант - вычисление случайного индекса
        random_nouns = nouns[random_idx] # не лучший вариант - используем случайный индекс

        random_adverbs = choice(adverbs) # вариант более простой choice()
        random_adjectives = choice(adjectives) # вариант более простой choice()
        print(random_nouns, random_adverbs, random_adjectives)

        i_count += 1
    return None

print('get_jokes(2)')
get_jokes(2)
print()
print('get_jokes(5)')
get_jokes(5)
print()
print('Документирование функции...')
print(help(get_jokes))

print('End')