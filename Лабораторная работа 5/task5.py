import random
import string


def get_random_password(x: int = 8) -> str:  # TODO написать функцию генерации случайных паролей
    return random.sample([lower_letter for lower_letter in string.ascii_lowercase] +
                         [upper_letter for upper_letter in string.ascii_uppercase] +
                         [digit for digit in string.digits],
                         k=x)


print(get_random_password())
