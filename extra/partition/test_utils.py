
# Routine used in my_tests.py to read input-data from a string!

def from_data_to_items(input_data):
    lines = input_data.split('\n')

    first_line = lines[0].split()
    numValues  = int(first_line[0])
    left       = int(first_line[1])
    right      = int(first_line[2])

    items = []
    for i in range(1, numValues+1):
        line  = lines[i]
        parts = line.split()
        items.append(int(parts[0]))
    assert right <= len(items)-1

    return items, left, right