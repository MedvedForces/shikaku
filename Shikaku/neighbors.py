import shikaku_map

def neighbors(cell, map):
    x, y = cell
    for dx, dy in shikaku_map.DIRS:
        koordinates = (x + dx, y + dy)
        if koordinates in map:
            yield koordinates
