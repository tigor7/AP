# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_memoization(items):
    mem = {}
    taken = []

    def t(n):
        # Primera fase: Calculamos la recurrencia guardando en
        # el diccionario la solución optima de cada subproblema.
        # ...
        #   Aviso: Para resolver este ejercicio no es valido
        #          utilizar el soporte de @functools
        if n in mem:
            return mem[n]

        mem[n] = max(t(n - 1), t(n - 2) + items[n]) if n >= 0 else 0
        return mem[n]

    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de las casas elegidas por el ladrón para
        # obtener el máximo beneficio. En el ejemplo de las
        # transparencias el contenido de esta lista es: [2,5]
        # (la segunda casa y la quinta casa).
        # ...
        i = len(items) - 1
        b = mem[i]
        while i > 0 and b > 0:
            if mem[i] <= b and mem[i] != mem[i-1]:
                taken.insert(0, i + 1)
                b = b - items[i]
            i -= 1
    n = len(items) - 1
    
    max_benefit = t(n)
    fill_taken()
    
    return max_benefit, taken
