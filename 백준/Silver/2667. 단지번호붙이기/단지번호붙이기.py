n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

call_count = 0    
    
def dfs(x, y):
    global call_count
    if x >= n or y >= n or x <= -1 or y <= -1:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        call_count += 1
        
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result_house = []
result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            result_house.append(call_count)
            call_count = 0  

result_house.sort()
print(result)
for i in result_house:
    print(i)