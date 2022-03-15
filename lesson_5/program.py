def get_mark(
        points: int,
        bonus_points: int=0,
        minus_points: int=0) -> int:
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

round()