l, r = map(str, input().split())

count = 0

if min(l.count('8'), r.count('8')) == 0:
    print(0)
    
else:
    if len(l) != len(r):
        l = l.zfill(len(r))
    
    for i in range(len(r)):
        if l[i] == '8' and r[i] == '8':
            count += 1
        elif l[i] != r[i]:
            break
    
    print(count)