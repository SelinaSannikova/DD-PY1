def delete(list_, index=None):
    if index is not None:
        n = list_[:index]
        x = list_[index+1:]
        last_ = n + x
        return last_
    else:
        return list_  # TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4]))  # [0, 1, 2, 3]
