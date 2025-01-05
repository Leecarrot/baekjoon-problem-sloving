from collections import deque

m, n, h = map(int, input().split())

graph = []

for i in range(h):
    graph.append([])
    for j in range(n):
        graph[i].append(list(map(int, input().split())))
        
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in  range(h)]


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    que = deque()
    # 익은 토마토의 시작점
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    que.append((k, j, i))
                    visited[i][j][k] = True
    
    while que:
        x, y, z = que.popleft()
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                if graph[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
                    visited[nz][ny][nx] = True
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    que.append((nx, ny, nz))


bfs()
ans = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(j))
print(ans-1)