from math import pi


def greet_user(name):
    print(f'Hello {name}!')


def return_bigger(a, b):
    return a if a > b else b


def twice_pi():
    return pi * 2


def code_me_later(par1, par2):
    # TODO
    pass


# Typove anotace take na kodim
# uplně na konci kapitoly https://kodim.cz/czechitas/progr2-python/zaklady-programovani-2/funkce
def get_mark(
        points: int,
        bonus_points: int = 0,
        minus_points: int = 0) -> int:
    if points + bonus_points <= 60:
        mark = 5
    elif points + bonus_points <= 70:
        mark = 4
    elif points + bonus_points <= 80:
        mark = 3
    elif points + bonus_points <= 90:
        mark = 2
    else:
        mark = 1
    return mark

print(get_mark(30, 0, 20))
