def next_number(digits, base):
    """
    :param digits: list containing all the digits of a number
                   in the given base
    :param base: numeric base of the number
    :return: list representing the next value of the number

     Example: digits = [0, 1, 0, 1]   number 5
                base = 2

              returns [0, 1, 1, 0]    number 6
    """

    next_digits = digits.copy()
    for i in range(len(next_digits) - 1, -1, -1):
        if next_digits[i] + 1 < base:
            next_digits[i] += 1
            break
        next_digits[i] = 0


    return next_digits

# ----------------------------------------------------------

class My_Iterator:

    def __init__(self, num_digits, base):
        self.num_digits = num_digits
        self.base = base
        self.curr = [0] * num_digits

    def next(self):
        for i in range(self.base ** self.num_digits):
            yield self.curr
            self.curr = next_number(self.curr, self.base)
        return
