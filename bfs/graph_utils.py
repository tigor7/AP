import networkx as nx

def build_graph():
    # Añade aqui el código que hiciste en el ejercicio del 
    first_line = input().split()
    num_nodes  = int(first_line[0])
    num_edges  = int(first_line[1])

    # Paso 1: Crear el grafo no-dirigido con sus vértices
    graph = nx.Graph()
    graph.add_nodes_from([i for i in range(1, num_nodes)])

    # Paso 2: Añadirle las aristas
    for _ in range(num_edges):
        line = input().split()
        first = int(line[0])
        second = int(line[1])
        graph.add_edge(first, second)

    return graph
