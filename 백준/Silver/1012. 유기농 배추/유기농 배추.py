from collections import deque

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    
    graph = [[0 for _ in range(m)] for _ in range(n)]
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
        
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        que = deque([(x, y)])
        
        while que:
            x, y = que.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        que.append((nx, ny))
        return 1
    
    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                result += bfs(i, j)
    
    print(result)