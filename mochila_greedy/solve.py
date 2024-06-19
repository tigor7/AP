def density(item):
    return item[0] / item[1]

def solve(items, capacity):
    taken = []
    value = 0

    items_copy = [(item[0], item[1], index) for index, item in enumerate(items)]
    items_copy.sort(key=density, reverse=True)

    for item in items_copy:
        if item[1] <= capacity:
            taken.append(item[2]+1)
            capacity -= item[1]
            value += item[0]
    return taken, value
