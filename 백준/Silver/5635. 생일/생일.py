n = int(input())
n_dict = {}

for _ in range(n):
    a, b, c, d = input().split()
    n_dict[a] = [int(b), int(c), int(d)]

# 키와 값을 모두 포함한 형태로 정렬
sorted_items = sorted(n_dict.items(), key=lambda x: (x[1][2], x[1][1], x[1][0]))

print(sorted_items[-1][0])
print(sorted_items[0][0])