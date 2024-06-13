# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_tabulation(items):
    table = []
    taken = []
    
    def fill_table():
        # Primera fase: Rellenamos la lista 'table' con las
        # soluciones de todos los subproblemas (o sea, los
        # beneficios que puede conseguir el ladrón).
        # ...
        table.append(items[0])
        table.append(max(items[0], items[1]))
        for i in range(2, len(items)):
            table.append(max(table[i - 1], table[i -2] + items[i]))

    def fill_taken():
        # Segunda fase: Rellenamos la lista 'taken' con el
        # indice de las casas elegidas por el ladrón para
        # obtener el máximo beneficio. En el ejemplo de las
        # transparencias el contenido de esta lista es: [2,5]
        # (la segunda casa y la quinta casa).
        # ...
        i = len(items) - 1
        b = table[i]
        while i > 0 and b > 0:
            if table[i] <= b and table[i] != table[i-1]:
                taken.insert(0, i + 1)
                b = b - items[i]
            i -= 1

    fill_table()
    fill_taken()
    return table[len(items) - 1], taken
