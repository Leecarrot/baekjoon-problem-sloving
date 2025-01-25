n = int(input())
graph = []

for _ in range(n):
    graph.append(list(input()))
    
# 심장 위치 구하기
flag = False

for i in range(n):
    for j in range(len(graph[0])):
        if graph[i][j] == '*':
            a = i + 1
            b = j
            flag = True
    if flag:
        break

arm1_count = 0
for i in range(0, b):
    if graph[a][i] == '*':
        arm1_count += 1
        
arm2_count = 0
for i in range(b + 1, len(graph[0])):
    if graph[a][i] == '*':
        arm2_count += 1
    
ff = 0
for i in range(a + 1, n):
    if graph[i][b] == '*':
        ff += 1
        d = i
        g = b
        
ff1 = 0
ff2 = 0
for i in range(d + 1, n):
    if graph[i][b - 1] == '*':
        ff1 += 1
        
    if graph[i][b + 1] == '*':
        ff2 += 1

print(a + 1, b + 1)
print(arm1_count, arm2_count, ff, ff1, ff2)