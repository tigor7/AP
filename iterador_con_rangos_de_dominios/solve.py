

class My_Iterator:
    def __init__(self, num_digits, min_values, max_values):
        self.num_digits = num_digits
        self.min_values = min_values
        self.max_values = max_values
        self.iterations = 1
        for i in range(num_digits):
            self.iterations *= max_values[i] - min_values[i] + 1

    def next(self):
        curr = self.min_values.copy()
        for _ in range(self.iterations):
            yield curr
            for i in range(self.num_digits - 1, -1, -1):
                if curr[i] + 1 <= self.max_values[i]:
                    curr[i] += 1
                    break
                curr[i] = self.min_values[i]
