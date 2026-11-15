from .generate import generate_full_map
from .solve_task import solve
from .validate import validate
from .shikaku_map import print_map

def main():
    print(f"Привет, это игра shikaku на поле из шестиугольников.\n"
          f"Карта рандомно генерируется.\n"
          f"Для начала укажи размер карты и "
          f"кол-во решений, которое хочешь найти:")
    map_size = int(input("Укажи размер карты: "))
    count_solves = int(input("Укажи кол-во решений: "))
    map, numbers = generate_full_map(map_size)
    valid, error = validate(map, numbers)
    if not valid:
        print("Ошибка:", error)
        return

    print("Карта:")
    print_map(map, numbers)

    all_solves = solve(map, numbers, count_solves)
    if not all_solves:
        print("Решений нет!")
    else:
        print(f"\nНайдено решений: {len(all_solves)}")
        for i in range(len(all_solves)):
            print(f"\nРешение {i + 1}:")
            print_map(map, numbers, all_solves[i])


if __name__ == "__main__":
    main()
