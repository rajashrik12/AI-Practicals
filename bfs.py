# Breadth First Search - Recursive version
# Explore all neighbors at current depth before going deeper.

from collections import deque  # Using queue for BFS

def bfs_recursive(queue, visited, graph):
    if not queue:
        return                 # If queue empty, all nodes visited
    vertex = queue.popleft()    # Get next node to explore
    print(vertex, end=" ")
    for neighbor in graph[vertex]:
        if neighbor not in visited:     # Visit unvisited neighbors
            visited.add(neighbor)
            queue.append(neighbor)
    bfs_recursive(queue, visited, graph) # Recursive call

# Adjacency list for undirected graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()
queue = deque(['A'])     # Start BFS with node 'A'
visited.add('A')

print("\nBFS traversal:")
bfs_recursive(queue, visited, graph)
