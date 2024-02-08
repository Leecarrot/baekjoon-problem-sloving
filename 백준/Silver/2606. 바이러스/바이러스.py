from collections import deque

n = int(input())
m = int(input())

graph = [[] for i in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n + 1):
    graph[i].sort()




def bfs(graph, visited, v):
    queue = deque([v])
    visited[v] = True
    
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    return visited.count(True) - 1

visited = [False] * (n+1)            
print(bfs(graph, visited, 1))