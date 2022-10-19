list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

even = 0
odd = 0

for numbers in list_:
    if numbers % 2 == 0:
        even += 1
for numberss in list_:
    if numberss % 3 == 0:
        odd += 1  # TODO завести отдельные счетчики для четных и нечетных чисел

for numbers in list_:
    if numbers % 2 == 0:
        even += 1
    else:
        odd += 1  # TODO с помощью одного цикла перебрать все числа и посчитать количество четных и нечетных

if even > odd:
    print("Четных чисел больше")
elif odd > even:
    print("Нечетных чисел больше")
else:
    print("Четных и нечетных одинаковое количество")  # TODO вывести каких чисел больше
