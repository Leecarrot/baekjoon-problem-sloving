n, k = map(int, input().split())
placement = list(input())
ans = 0

for idx in range(n):
    if placement[idx] == 'P':
        for i in range(max(idx-k, 0), min(idx+k+1, n)):
            if placement[i] == 'H':
                placement[i] = 0
                ans += 1
                break
print(ans)