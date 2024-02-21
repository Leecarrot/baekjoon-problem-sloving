n = int(input())
result = 0
count = 0

if n == 1:
    print(1)
else:
    for i in range(1, n+1):
        if result <= n:
            result += i
            count += 1
        else:
            break
    print(count - 1)