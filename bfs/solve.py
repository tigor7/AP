import networkx   as nx
from sys          import maxsize as infinite
from simple_queue import *

def bfs_path_length(graph, first_node):
    """
    Compute the shortest path length of the non-directed graph G
    starting from node first_node. Return a dictionary with the
    distance (in number of steps) from first_node to all the nodes.
    """

    distance = {}

    for node in graph.nodes():
        distance[node] = infinite

    distance[first_node] = 0
    seen = []
    q = Queue()
    q.enqueue(first_node)
    while not q.isEmpty():
        curr = q.dequeue()
        for neighbor in graph.adj[curr]:
            if neighbor not in seen:
                q.enqueue(neighbor)
                seen.append(neighbor)
                distance[neighbor] = distance[curr] + 1




    return distance
