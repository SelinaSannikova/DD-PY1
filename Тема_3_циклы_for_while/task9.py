surname_list = [  # список фамилий Санкт-Петербурга
    "Иванов",
    "Васильев",
    "Петров",
    "Смирнов",
    "Михайлов",
    "Фёдоров",
    "Соколов",
    "Яковлев",
    "Попов",
    "Андреев",
    "Алексеев",
    "Александров",
    "Лебедев",
    "Григорьев",
    "Степанов",
    "Семёнов",
    "Павлов",
    "Богданов",
    "Николаев",
    "Дмитриев",
    "Егоров",
    "Волков",
    "Кузнецов",
    "Никитин",
    "Соловьёв"
]

for number_surname, surname in enumerate(surname_list, start=1):  # start по умолчанию равен 0, но можно задать произвольный
    print(number_surname, surname)
