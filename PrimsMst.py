# Prim's Algorithm
# Start from a node and expand the minimum cost edge.

import heapq

def prim(graph):
    start_node = list(graph.keys())[0]
    visited = set([start_node])
    edges = [
        (cost, start_node, to)
        for to, cost in graph[start_node]
    ]
    heapq.heapify(edges)   # Make a min-heap
    mst = []               # Store MST edges

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            for to_next, cost in graph[to]:
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))
    return mst

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

print("\nPrim's MST:")
print(prim(graph))
