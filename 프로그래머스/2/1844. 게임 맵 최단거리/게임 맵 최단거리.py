from collections import deque

def solution(maps):
    visited = [[False for i in range(len(maps[0]))] for j in range(len(maps))]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    def dfs(x, y):
        que = deque()
        que.append((x, y))
        
        while que:
            x, y = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[nx]):
                    if maps[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        maps[nx][ny] = maps[x][y] + 1
                        que.append((nx, ny))
        if visited[len(maps) - 1][len(maps[0]) -1] == False:
            return -1
        else:
            return maps[len(maps) - 1][len(maps[0]) -1]
    return dfs(0, 0)
            