# graph = {
#   '5' : ['3', '7'],
#   '3' : ['2', '4'],
#   '7' : ['8'],
#   '4' : ['8'],
#   '2' : [],
#   '8' : []
#  }


# visited = []
# queue = []

# def bfs(visited, graph, node):
#   visited.append(node)
#   queue.append(node)
#   while queue:
#     m = queue.pop(0)
#     print(m, end = " ")

#     for neighbour in graph[m]:
#       if neighbour not in visited:
#         visited.append(neighbour) 
#         queue.append(neighbour)

# print("The bfs is: ")
# bfs(visited, graph, '5')



def bfs_recursive(visited, graph, queue):
    if not queue:  
        return
    node = queue.pop(0)  
    print(node, end=" ")  
    visited.append(node)  
    for neighbour in graph[node]:  
        if neighbour not in visited and neighbour not in queue:
            queue.append(neighbour)
    bfs_recursive(visited, graph, queue)

def bfs(graph, start):
    visited = []  
    queue = [start]  
    bfs_recursive(visited, graph, queue)  

graph = {
  '5' : ['3', '7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '4' : ['8'],
  '2' : [],
  '8' : []
 }

print("The BFS is:")
bfs(graph, '5')
