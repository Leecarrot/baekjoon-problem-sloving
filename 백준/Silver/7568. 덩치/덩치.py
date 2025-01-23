n = int(input())
n_list = []
for _ in range(n):
    x, y = map(int, input().split())
    n_list.append((x, y))
    


for i in range(n):
    k = 1
    for j in range(n):
        if n_list[i][0] < n_list[j][0] and n_list[i][1] < n_list[j][1]:
            k += 1
    print(k, end = ' ')