
def validate(map, numbers):
    for x, y in numbers.items():
        if x not in map:
            return (False, f"клетка {x} не найдена!")
        if y < 0:
            return (False, f"некорректный размер {y}!")
    if sum(numbers.values()) != len(map):
        return (False, "сумма чисел не равна количеству шестиугольников!")
    return (True, None)