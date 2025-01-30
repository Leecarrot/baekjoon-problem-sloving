t, r = map(str, input().split())

count = 0

a = t.zfill(len(r))
    
for i in range(len(r)):
    if a[i] == '8' and r[i] == '8':
        count += 1
        
    elif a[i] != r[i]:
        break
    
print(count)