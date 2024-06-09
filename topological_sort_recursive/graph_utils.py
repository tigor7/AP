import networkx as nx

def build_digraph_with_weights():
    DG = nx.DiGraph()

    first_line = input().split()
    num_nodes = int(first_line[0])
    num_edges = int(first_line[1])

    DG.add_nodes_from([x for x in range(1, num_nodes + 1)])

    for _ in range(num_edges):
        line = input().split()
        DG.add_edge(int(line[0]), int(line[1]), weight=int(line[2]))

    return DG
