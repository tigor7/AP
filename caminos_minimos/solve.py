import networkx as nx
from sys import maxsize as infinite

def solve(graph, u, v):
    solutions_list = []

    solution = []
    curr_distance = 0
    best_distance = 1000

    seen = []

    def dfs(node):
        nonlocal curr_distance
        nonlocal best_distance
        seen.append(node)
        solution.append(node)
        if node == v:
            if curr_distance > best_distance:
                return
            if curr_distance < best_distance:
                solutions_list.clear()
                best_distance = curr_distance
            solutions_list.append(solution.copy())
            return

        for neighbor, attr in graph.adj[node].items():
            if neighbor not in seen:
                curr_distance += attr["weight"]
                dfs(neighbor)
                curr_distance -= attr["weight"]
                solution.pop()
                seen.pop()

    dfs(u)
    return solutions_list
