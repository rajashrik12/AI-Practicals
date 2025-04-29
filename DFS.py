# Depth First Search - Recursive version
# We explore a node, then recursively explore its neighbors.

def dfs(graph, vertex, visited):
    if vertex not in visited:           # If vertex is not visited
        print(vertex, end=" ")           # Print the vertex
        visited.add(vertex)              # Mark vertex as visited
        for neighbor in graph[vertex]:   # Visit all the neighbors
            dfs(graph, neighbor, visited)

# Adjacency list for undirected graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()                         # To keep track of visited nodes
print("DFS traversal:")
dfs(graph, 'A', visited)                # Start DFS from node 'A'
