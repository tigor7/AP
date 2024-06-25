import networkx   as nx
from simple_queue import *

def bfs_path(graph, first_node, last_node):
    """
    Compute the shortest path from the first_node to the last_node
    of the non-directed graph G. Return a list with the nodes.
    """
    route = []

    distance = {}
    distance[first_node] = 0

    seen = {first_node}
    q = Queue()
    q.enqueue(first_node)

    while not q.isEmpty():
        node = q.dequeue()
        for neighbor in graph.adj[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                q.enqueue(neighbor)
                distance[neighbor] = distance[node] + 1

    route.append(last_node)
    curr = last_node
    while curr != first_node:
        for neighbor in graph.adj[curr]:
            if distance[neighbor] == distance[curr] - 1:
                curr = neighbor
                route.insert(0, curr)

    return route
