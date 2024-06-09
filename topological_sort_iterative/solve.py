import networkx as nx
from simple_stack import Stack

def dfs_topological_sort(graph):
    """
    Compute one topological sort of the given graph.
    """
    
    # La solucion que retorna esta función es un diccionario de Python.
    #   * La clave del diccionario es el número del nodo
    #   * El valor es el orden topologico asignado a ese nodo
    # 
    # Por ejemplo, si tenemos el siguiente grafo dirigido con 3 vertices:
    #                    3 ---> 2 ---> 1
    # ... el orden topologico es:
    #                El vértice 3 va en la primera posición
    #                El vértice 2 en la segunda posición
    #                El vértice 1 en la tercera posición
    # Con lo que debemos devolver un diccionario con este contenido:
    #     {1: 3, 2: 2, 3: 1}

    N = graph.number_of_nodes()
    
    visibleNodes = set()

    order = {}

    def dfs_iterative(u):
        nonlocal N
        S = Stack()
        S.push(u)
        while not S.isEmpty():
            node = S.peek()
            visibleNodes.add(node)
            for neighbor in graph.adj[node]:
                if neighbor not in visibleNodes:
                    S.push(neighbor)
            if S.peek() == node:
                order[node] = N
                N -= 1
                S.pop()

    for node in graph.nodes:
        if node not in visibleNodes:
            dfs_iterative(node)

    return order
