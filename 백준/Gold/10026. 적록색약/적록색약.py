import sys
sys.setrecursionlimit(10 ** 6) 

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(str, input())))
    
graph2 = [['R' if cell == 'G' else cell for cell in row] for row in graph]
    
def dfs(color, x, y, graph):
    if x >= n or y >= n or x <= -1 or y <= -1:
        return False
    
    if graph[x][y] == color:
        graph[x][y] = 'T'
        
        dfs(color, x - 1, y, graph)
        dfs(color, x + 1, y, graph)
        dfs(color, x, y - 1, graph)
        dfs(color, x, y + 1, graph)
        return True
    return False


colors = ['R', 'G', 'B']
graph_list = [graph, graph2]

for graph in graph_list:
    count = 0
    for color in colors:
        for i in range(n):
            for j in range(n):
                if dfs(color, i, j, graph) == True:
                    count += 1
    print(count, end = ' ')