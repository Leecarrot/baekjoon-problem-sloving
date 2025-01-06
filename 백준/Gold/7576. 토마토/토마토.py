from collections import deque

n, m = map(int, input().split())
graph = []
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
for _ in range(m):
    graph.append(list(map(int, input().split())))
    
def dfs():
    que = deque()
        
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                que.append((i, j))
        
    while que:
        x, y = que.popleft()
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
                
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    que.append((nx, ny))
    
dfs()
    
result = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] ==0:
            print(-1)
            exit(0)
    result = max(max(graph[i]), result)

print(result - 1)