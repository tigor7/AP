from my_iterator import *

def check_combination(comb):
    for i in range(len(comb) - 1):
        for j in range(i + 1, len(comb)):
            dis = j - i
            if comb[i] == comb[j] or comb[i] == comb[j] + dis or comb[i] == comb[j] - dis:
                return False

    return True

def solve(num_queens):
    """
    Using your brute force iterator compute all the
    solutions to place the given number of queens in
    a square board.

    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions

    For example, if num_queens = 4 there are two solutions,
    and it returns:
       solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]

    """

    solutions_list = []

    iterator = My_Iterator(num_queens, num_queens)
    for combination in iterator.next():
        if check_combination(combination):
            solutions_list.append(combination)


    return solutions_list
