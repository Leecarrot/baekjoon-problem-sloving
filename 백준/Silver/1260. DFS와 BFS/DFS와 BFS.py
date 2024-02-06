from collections import deque

n,m,v = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
for i in range(n + 1):
    graph[i].sort()

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
def bfs(graph, v, visited):
    
    queue = deque([v])
    
    visited[v] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
visited = [False] * (n+1)
dfs(graph, v, visited)
print(end = '\n')
visited = [False] * (n+1)
bfs(graph, v, visited)