import sys
sys.setrecursionlimit(10 ** 6)

m, n = map(int, input().split())

graph = []

for _ in range(m):
    graph.append(list(map(int, input())))
    
def dfs(x, y):
    a = []
    if x >= m or y >= n or x <= -1 or y <= -1:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 'goal'
        
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

for j in range(n):
    dfs(0, j)

if 'goal' in graph[m - 1]:
    print('YES')
else:
    print('NO')