import sys
sys.setrecursionlimit(10 ** 6) 

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    
max_num = 0

for a in range(len(graph)):
    for b in range(len(graph)):
        if graph[a][b] >= max_num:
            max_num = graph[a][b]


def dfs(x, y, num):
    if x >= n or y >= n or x <= -1 or y <= -1:
        return False
    
    if graph[x][y] > int(num) and not visited[x][y]:
        visited[x][y] = True
        
        dfs(x - 1, y, num)
        dfs(x + 1, y, num)
        dfs(x, y - 1, num)
        dfs(x, y + 1, num)
        return True
    return False

final_max = 0

for num in range(0, max_num):
    visited = [[False for i in range(n)] for i in range(n)]
    count= 0
    for i in range(n):
        for j in range(n):
            if dfs(i, j, num) == True:
                count += 1
    if count >= final_max:
        final_max = count

print(final_max)