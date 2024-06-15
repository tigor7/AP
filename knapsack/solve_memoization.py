
def solve_memoization(items, capacity):
    taken = []
    mem={}

    def t(n,w):
        # Primera fase: Calculamos la recurrencia guardando en
        # el diccionario la solución optima de cada subproblema.
        #   Aviso: Para resolver este ejercicio no es valido
        #          utilizar el soporte de @functools
        # ...
        if (n, w) in mem:
            return mem[(n, w)]

        if n < 0:
            result =  0
        elif w < items[n].weight:
            result = t(n-1, w)
        else:
            result = max(t(n - 1, w), t(n - 1, w - items[n].weight) + items[n].value)
        mem[(n, w)] = result
        return result


    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de los items elegidos.
        # ...

        n = len(items) - 1
        w = capacity
        while n >= 0:
            if mem[(n, w)] != mem[(n - 1, w)]:
                w -= items[n].weight
                taken.insert(0, n + 1)
            n -= 1

    n = len(items)-1

    max_benefit = t(n,capacity)
    fill_taken()

    return max_benefit, taken
