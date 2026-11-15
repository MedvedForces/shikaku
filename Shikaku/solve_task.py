from find_objects import find_regions

def enumeration(current_number, numbered, variants,
                    used, current_solve, map, all_solves, max_solves_count = None):
    if max_solves_count and len(all_solves) >= max_solves_count:
        return
    if current_number == len(numbered):
        if set(used) == set(map):
            all_solves.append(current_solve.copy())
        return

    koordinates, _ = numbered[current_number]
    for r in variants[koordinates]:
        if any(x in used for x in r):
            continue
        for i in r:
            used.append(i)
        current_solve[koordinates] = r
        enumeration(current_number + 1, numbered, variants,
                  used, current_solve, map, all_solves, max_solves_count)
        for i in r:
            used.remove(i)
        current_solve.pop(koordinates)

def solve(map, numbers, max_solves_count = None):
    all_solves = []
    numbered = list(numbers.items())
    variants = {}

    for koordinates, size in numbered:
        regs = find_regions(koordinates, size, map)
        if not regs:
            return []
        variants[koordinates] = regs

    enumeration(0, numbered, variants, [], {}, map, all_solves, max_solves_count)
    return all_solves
