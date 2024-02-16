n = int(input())

result = []
for i in range(n):
    a, b = input().split()
    result.append((i, int(a), b))

output = sorted(result, key = lambda x:(x[1], x[0]))

for i in output:
    print(i[1], i[2])