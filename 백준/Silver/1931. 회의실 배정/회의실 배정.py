n = int(input())
times = []

for i in range(n):
    times.append(list(map(int, input().split())))
times = sorted(times, key = lambda x: (x[1], x[0]))

start = times[0][1]
cnt = 1

for i in times[1:]:
    if i[0] >= start:
        cnt += 1
        start = i[1]
    else:
        continue

print(cnt)