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
    'I':[],
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, 'A')