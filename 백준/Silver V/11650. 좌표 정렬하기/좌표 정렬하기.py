result = []

for _ in range(int(input())):
    a, b = input().split()
    result.append((int(a), int(b)))

output = sorted(result, key = lambda x: (x[0], x[1]))
for i in output:
    print(i[0], i[1])