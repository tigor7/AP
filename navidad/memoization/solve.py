
def solve(p, q):
    mem = {}
    def memSolve(p, q):
        if (p, q) not in mem:
            if p == q:
                mem[(p, q)] = 1
            else:
                s = 0
                for k in range(p, q):
                    s += memSolve(p, k) + memSolve(k + 1, q)
                mem[(p, q)] = max(memSolve(p+1, q), s)
        return mem[(p, q)]

    memSolve(p, q)
    return mem[(p, q)]
