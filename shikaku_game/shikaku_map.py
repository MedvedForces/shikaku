DIRS = [(1,1), (-1,1), (0,1), (1,0), (0,-1), (-1,0)]

def print_map(map, numbers, solve = None):
    sort_map = sorted(map)
    for cell in sort_map:
        if solve:
            what_region = None
            for (x, y) in solve.items():
                if cell in y:
                    what_region = x
            print(f"{cell}: {what_region}")
        else:
            if cell in numbers:
                value = numbers[cell]
            else:
                value = '.'
            print(f"{cell}: {value}")