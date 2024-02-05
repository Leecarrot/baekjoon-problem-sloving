a = int(input())
b = list(map(int, input().split()))
c = list(map(int, input().split()))

start = c[0] * b[0] 
c.pop()
print(min(c[1:]) * sum(b[1:]) + start)