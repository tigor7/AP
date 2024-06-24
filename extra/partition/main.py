from solve    import *
from my_tests import *

# Check my tests
tests = My_Tests()
tests.test_from_data_to_item()
tests.test_1()
# ..             # Add more tests as you consider convenient

first_line = input().split()
numValues  = int(first_line[0])
left       = int(first_line[1])
right      = int(first_line[2])

items = []
for j in range(1, numValues+1):
    parts = input().split()
    items.append(int(parts[0]))
assert right <= len(items)-1

# Solve the exercise
print("Here")
pos_pivote = partition(items, left, right)
print("Here")
print(pos_pivote, items)
