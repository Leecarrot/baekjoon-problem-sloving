from collections import deque

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
    
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
    
def bfs(x, y, high):
    que = deque([(x, y)])
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > high and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx, ny))
    return 1

final = []
for g in graph:
    for j in g:
        final.append(j)
        
final = set(final)
final.add(0)


li = []
for a in final:
    visited = [[False for _ in range(n)] for _ in range(n)]  # 방문 배열 초기화
    result = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > a and not visited[i][j]:
                result += bfs(i, j, a)
    li.append(result)


print(max(li))