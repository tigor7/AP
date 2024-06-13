
def solve(items):

    pass


first_line = input().split()
item_count = int(first_line[0])

items = []
for i in range(1, item_count+1):
    parts = input().split()
    items.append(int(parts[0]))

solve(items)

# Comenzamos programando la recurrencia mediante tabulation
# value1, taken1 = solve(items)
# print(value1)
# print(taken1)
