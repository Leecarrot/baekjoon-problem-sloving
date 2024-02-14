result = []

for _ in range(int(input())):
    a = input()
    result.append((a, int(len(a))))

out = sorted(set(result), key = lambda x: (x[1], x[0]))

for i in out:
    print(i[0])