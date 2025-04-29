# A* Algorithm
# Uses priority queue and heuristic to find shortest path.

from queue import PriorityQueue

def heuristic(a, b):
    # Manhattan distance (Sum of X and Y distances)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal, graph):
    queue = PriorityQueue()
    queue.put((0, start))  # Start node has priority 0
    came_from = {}         # To reconstruct the path
    cost_so_far = {start: 0}  # Cost to reach each node

    while not queue.empty():
        current = queue.get()[1]

        if current == goal:
            break  # Goal reached

        for neighbor in graph.get(current, []):
            new_cost = cost_so_far[current] + 1  # Assuming each move costs 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor)  # f(n) = g(n) + h(n)
                queue.put((priority, neighbor))
                came_from[neighbor] = current

    # Reconstruct path
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# Example graph as 2D points
graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (1, 1)],
    (1, 0): [(0, 0), (1, 1), (2, 0)],
    (1, 1): [(0, 1), (1, 0), (2, 1)],
    (2, 0): [(1, 0)],
    (2, 1): [(1, 1)]
}

start = (0, 0)
goal = (2, 1)

print("\nA* Path from", start, "to", goal, ":")
print(a_star(start, goal, graph))
