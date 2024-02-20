n = int(input())
result = []

for i in range(n):
    a = int(input())
    result.append(a)
    
result.sort(reverse = True)

out = []

for i in range(n):
    out.append((i+1) * result[i])
    
print(max(out))