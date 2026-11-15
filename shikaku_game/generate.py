from .neighbors import neighbors
import random

def generate_cell_map(radius):
    map = []
    for x in range(-radius + 1, radius):
        for y in range(-radius + 1, radius):
            if abs(x + y) < radius:
                map.append((x, y))
    return map

def generate_full_map(radius = 2):
    map = generate_cell_map(radius)
    not_used = list(map)
    regions = []

    while not_used:
        start = random.choice(not_used)
        size_region = min(random.randint(1, 3), len(not_used))
        current_region_demo = [start]
        cells_in_current_region = []
        for cell in neighbors(start, map):
            if cell in not_used:
                cells_in_current_region.append(cell)

        while cells_in_current_region and len(current_region_demo) < size_region:
            cell = random.choice(cells_in_current_region)
            current_region_demo.append(cell)

            for i in neighbors(cell, map):
                if (i in not_used and i not in cells_in_current_region
                        and i not in current_region_demo):
                    cells_in_current_region.append(i)

            cells_in_current_region = [
                cell for cell in cells_in_current_region
                if cell not in current_region_demo
            ]

        regions.append(current_region_demo)
        not_used = [cell for cell in not_used
                    if cell not in current_region_demo]

    numbers = {}

    for cell in regions:
        a = random.choice(cell)
        numbers[a] = len(cell)

    region_cells_sum = sum(numbers.values())
    cells_left = len(map) - region_cells_sum
    if cells_left > 0:
        for cell in map:
            if cell not in numbers:
                numbers[cell] = 1
                cells_left -= 1
                if cells_left == 0:
                    break

    return (map, numbers)