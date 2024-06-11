def solve(items):
    """
    Sort the given list of items in ascending order
    """

    def merge(left, mid, right):
        left_pointer = left
        right_pointer = mid + 1

        copy = items.copy()

        for i in range(left, right + 1):
            if left_pointer == mid + 1:
                items[i] = copy[right_pointer]
                right_pointer += 1
            elif right_pointer == right + 1:
                items[i] = copy[left_pointer]
                left_pointer += 1
            elif copy[left_pointer] < copy[right_pointer]:
                items[i] = copy[left_pointer]
                left_pointer += 1
            else:
                items[i] = copy[right_pointer]
                right_pointer += 1

    def merge_sort(left, right):
        if left >= right:
            return
        mid = left + (right - left) // 2
        merge_sort(left, mid)
        merge_sort(mid + 1, right)
        merge(left, mid, right)

    merge_sort(0, len(items) - 1)
