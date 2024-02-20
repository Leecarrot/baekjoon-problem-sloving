n = int(input())

up = list(map(int, input().split()))
down = list(map(int, input().split()))

up.sort(reverse = True)
down.sort()

result = 0

for i in range(n):
    result += up[i] * down[i]

print(result)