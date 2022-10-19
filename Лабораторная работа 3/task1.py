src = not False and True or False and not True

ur_result = 'True and True or False and False'
ur_result = 'True or False'
ur_result = 'True'  # TODO расписать упрощение выражения

result = True  # TODO подставить результат выражения

print(src == result)
