import random


def get_unique_list_numbers() -> list[int]:  # TODO написать функцию для получения списка уникальных целых чисел
    numbers_list = []  # Список
    count = 0
    while count != 15:  # Условие из 15 элементов
        number = random.randint(-10, 10)  # Рандом
        if number not in numbers_list:
            numbers_list.append(number)
            count += 1
    return numbers_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
