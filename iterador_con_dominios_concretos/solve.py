

class My_Iterator:

    def __init__(self, num_digits, digit_values):
        self.num_digits = num_digits
        self.digit_values = digit_values
        self.iterations = 1
        for i in range(num_digits):
            self.iterations *= len(digit_values[i])

    def next(self):
        indexes = [0] * self.num_digits
        for _ in range(self.iterations):
            yield [self.digit_values[i][x] for i, x in enumerate(indexes)]
            for i in range(self.num_digits - 1, -1, -1):
                if indexes[i] + 1 < len(self.digit_values[i]):
                    indexes[i] += 1
                    break
                indexes[i] = 0
