from collections import deque

m, n, k = map(int,input().split())

graph = [[0 for i in range(n)] for i in range(m)]

for _ in range(k):
    x, y, x2, y2 = map(int, input().split())
    
    for i in range(y, y2):
        for j in range(x, x2):
            graph[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False for i in range(n)] for i in range(m)]


def bfs(x, y):
 
    count = 1
    que = deque()
    que.append((x, y))
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if -1 < nx < m and - 1 < ny < n:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    count += 1
                    visited[nx][ny] = True
                    que.append((nx, ny))
    return count

count = 0
a_list = []

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            a_list.append(bfs(i, j))
            
a_list.sort()
print(len(a_list))
for i in a_list:
    print(i, end = ' ')