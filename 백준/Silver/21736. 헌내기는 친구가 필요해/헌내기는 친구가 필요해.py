from collections import deque

n, m = map(int, input().split())
graph = []
visited = [[False for _ in range(m)] for _ in range(n)]
for _ in range(n):
    graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    que = deque([(x, y)])
    friend = 0
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if (graph[nx][ny] == 'O' or graph[nx][ny] == 'P') and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if graph[nx][ny] == 'P':
                        friend += 1
                    que.append((nx, ny))
                    
    return friend

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            visited[i][j] = True
            result = bfs(i, j)
            if result != 0:
                print(result)
            else:
                print('TT')