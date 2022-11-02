def get_count_char(str_):
    dict_ = {}
    str_ = str_.lower()
    DEFAULT_COUNT = 0
    for letter in str_:
        dict_[letter] = dict_.get(letter, DEFAULT_COUNT) + 1

    return dict_  # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def percent(dict_v):
    count_ = sum(dict_v.values())
    for v in dict_v.values():
        v = round(v / count_ * 100, 2)
    return dict_v
print(percent(dict_v))
