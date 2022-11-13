def get_count_char(str_):
    dict_ = {}
    default_count = 0
    for letter in str_.lower():
        if letter.isalpha():
            if letter in dict_:
                dict_[letter] += 1
            else:
                dict_[letter] = 1
        else:
            default_count += 1 * 100 / len(str_)
    percent(dict_, str_, default_count)
    return dict_


def percent(dict_, str_, default_count):
    dict_another = {}
    procent = 0
    for k, v in dict_.items():
        func = v * 100 / len(str_)
        dict_another[v] = func
        procent += func
        print(k, "-", round(func, 2), end='%  ')
    all_ = procent + default_count
    print("\n", int(all_), "%")


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print("\n", get_count_char(main_str))
