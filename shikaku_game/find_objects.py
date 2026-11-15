from .neighbors import neighbors

def dfs(region, start_cells_in_map, size, map, ans):
    if len(region) == size:
        ans.append(region.copy())
        return

    for cell in start_cells_in_map[:]:
        new_region = region + [cell]
        new_start_cells_in_map = start_cells_in_map[:]

        for neighbor in neighbors(cell, map):
            if neighbor not in new_start_cells_in_map and neighbor not in new_region:
                new_start_cells_in_map.append(neighbor)

        new_start_cells_in_map = [x for x in new_start_cells_in_map if x not in new_region]

        if len(new_region) + len(new_start_cells_in_map) >= size:
            dfs(new_region, new_start_cells_in_map, size, map, ans)


def find_regions(start, size, map):
    ans = []
    start_cells_in_map = list(neighbors(start, map))
    dfs([start], start_cells_in_map, size, map, ans)
    return ans
