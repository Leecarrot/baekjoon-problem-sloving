from collections import deque
import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(str, input())))
    
visited = [[False for i in range(m)] for i in range(n)]

ix = 0
iy = 0

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            ix = i
            iy = j
            
def bfs(x, y):
    que = deque()
    que.append((x, y))
    result = 0
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if (graph[nx][ny] == 'O' or graph[nx][ny] == 'I' or graph[nx][ny] == 'P') and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if graph[nx][ny] == 'P':
                        result += 1
                    que.append((nx, ny))
    if result == 0:
        print('TT')
    else:
        print(result)
                
bfs(ix, iy)