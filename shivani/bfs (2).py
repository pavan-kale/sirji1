from collections import deque

def bfs_recursive(graph, queue):
    if not queue:
        return
    node = queue.popleft()
    print(node)  
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    bfs_recursive(graph, queue)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Starting node for BFS
start_node = 'A'

# Initialize a queue for BFS and a set to keep track of visited nodes
queue = deque([start_node])
visited = {start_node}

# Perform BFS starting from the given node
bfs_recursive(graph, queue)
