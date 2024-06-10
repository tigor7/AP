def is_valid_solution(solution, level):
    for i in range(level - 1):
        for j in range(i + 1, level):
            dis = j - i
            if solution[i] == solution[j] or solution[i] == solution[j] + dis or solution[i] == solution[j] - dis:
                return False
    return True

def solve(num_queens):
    """
    Using backtracking compute all the solutions to place the
    given number of queens in a square board.

    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions

    For example, if num_queens = 4 there are two solutions,
    and it returns:
       solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]

    """

    solutions_list = []

    solution = [-1] * num_queens
    def dfs(level):
        if not is_valid_solution(solution, level):
            return
        if level == num_queens:
            solutions_list.append(solution.copy())
            return
        for i in range(num_queens):
            solution[level] = i
            dfs(level + 1)
        solution[level] = -1


    dfs(level=0)

    return solutions_list
