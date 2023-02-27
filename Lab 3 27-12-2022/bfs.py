graph = {
  'A' : ['B','C','D'],
  'B' : ['E', 'F'],
  'C' : [],
  'D' : ['G','H','I'],
    'G':['L'],
  'E' : ['J'],
  'F' : ['K'],
    'J':[],
    'K':[],
    'L':[],
    'H':[],
    'I':[]
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0)
    print (m, end = " ")  

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, 'A')