import sys

sys.setrecursionlimit(10000)

def dfs(x, y):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True
    return False

t = int(input())

for _ in range(t): 
    m, n, k = map(int, input().split())
    graph = [[0] * m for i in range(n)]

    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                result += 1
    print(result)