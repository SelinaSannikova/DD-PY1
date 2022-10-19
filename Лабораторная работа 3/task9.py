salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
current_spend = spend

for current_money in range(1, months + 1):  # Условие, цикл с заданным количеством шагов
    current_money = (current_spend - salary)  # Необходимая дельта
    current_spend = current_spend * (1 + increase)  # Текущие затраты каждый месяц
    need_money += current_money  # TODO Оформить решение

print(round(need_money))
