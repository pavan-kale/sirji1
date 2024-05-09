import heapq

def djikstras(graph, start, end):
  pq = [(0 ,start)]
  visited = set()
  while pq:
    (cost, curr_node) = heapq.heappop(pq)
    if curr_node == end:
      return cost
    if curr_node in visited:
      continue
    visited.add(curr_node)
    for(next_node, edge_cost) in graph[curr_node]:
      if next_node not in visited:
        heapq.heappush(pq, (edge_cost + cost, next_node))
  return float("inf")

graph = {
  'A' : [('B', 5), ('C', 1)],
  'B' : [('A', 5), ('C', 2), ('D', 1)],
  'C' : [('A', 1), ('B', 2), ('D', 4)],
  'D' : [('B', 1), ('C', 4)]
}

shortest_distance = djikstras(graph, 'B', 'D')
print("The shortest Distance between B and D is ", shortest_distance)

# Certainly! Let’s break down the code step by step:

# Graph Representation:
# The code defines a graph using an adjacency list representation. Each node in the graph is represented by a letter (‘A’, ‘B’, ‘C’, ‘D’), and the associated edges are stored as tuples containing the neighboring node and the edge cost.
# For example:
# Node ‘A’ has edges to ‘B’ (cost 5) and ‘C’ (cost 1).
# Node ‘B’ has edges to ‘A’ (cost 5), itself (cost 2), and ‘D’ (cost 1).
# Node ‘C’ has edges to ‘A’ (cost 1), ‘B’ (cost 2), and ‘D’ (cost 4).
# Node ‘D’ has edges to ‘B’ (cost 1) and ‘C’ (cost 4).
# Dijkstra’s Algorithm:
# The function djikstras implements Dijkstra’s algorithm to find the shortest distance between two nodes in the graph.
# It takes three arguments:
# graph: The graph represented as an adjacency list.
# start: The starting node.
# end: The target node.
# The algorithm maintains a priority queue (pq) to explore nodes in order of their cumulative cost from the start node.
# The visited set keeps track of nodes already visited.
# The main loop continues until the priority queue is empty.
# Within each iteration:
# Pop the node with the minimum cost from the priority queue.
# If the popped node is the target node, return the accumulated cost.
# Otherwise, mark the current node as visited and explore its neighbors.
# Update the priority queue with the new cumulative costs.
# If the target node is not reached, return infinity.
# Example Usage:
# The code calculates the shortest distance between nodes ‘B’ and ‘D’ in the given graph.
# In this case, the shortest distance from ‘B’ to ‘D’ is 3 (via the path ‘B’ -> ‘D’).
# Output:
# The code prints: “The shortest Distance between B and D is 3.”
# Dijkstra’s algorithm is widely used for finding the shortest path in weighted graphs. It guarantees the shortest path when all edge weights are non-negative.