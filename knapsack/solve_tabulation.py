
import numpy as np

def solve_tabulation(items, capacity):
    taken = []
    table = np.zeros((len(items)+1,capacity+1), dtype=int)

    def fill_table():
        for i in range(1, len(items) + 1):
            for w in range(1, capacity + 1):
                if w >= items[i - 1].weight:
                    table[i][w] = max(table[i - 1][w], table[i - 1][w - items[i - 1].weight] + items[i - 1].value)
                else:
                    table[i][w] = table[i - 1][w]

    def fill_taken():
        i = len(items)
        w = capacity
        while i >= 0:
            if table[i][w] != table[i-1][w]:
                taken.insert(0, i)
                w -= items[i - 1].weight
            i -= 1

    fill_table()
    fill_taken()
    return table[len(items)][capacity], taken
