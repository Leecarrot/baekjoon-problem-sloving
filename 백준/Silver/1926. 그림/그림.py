from collections import deque

n, m = map(int, input().split())

graph = []

visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))
    

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    que = deque()
    que.append((x, y))
    area = 1   
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
                
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    area += 1
                    visited[nx][ny] = True
                    que.append((nx, ny))
    return area

result = 0
zero_max = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            result += 1
            zero_max = max(dfs(i, j), zero_max)
    
print(result)
print(zero_max)