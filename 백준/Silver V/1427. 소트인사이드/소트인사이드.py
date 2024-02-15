n = input()
result = []

for i in n:
    result.append(int(i))

result.sort(reverse = True)

for j in result:
    print(j, end = '')