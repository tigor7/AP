
def solve(items, capacity):
    taken = []
    value = 0
    weight = 0

    best_value = 0
    best_taken = []


    def dfs(level):
        nonlocal value, weight, taken, best_value, best_taken
        if weight > capacity:
            return
        if value > best_value:
            best_value = value
            best_taken = taken.copy()
        if level == len(items):
            return
        taken.append(level + 1)
        value += items[level][0]
        weight += items[level][1]
        dfs(level + 1)
        value -= items[level][0]
        weight -= items[level][1]
        taken.pop()

        dfs(level + 1)

    dfs(0)
    return best_taken, best_value
