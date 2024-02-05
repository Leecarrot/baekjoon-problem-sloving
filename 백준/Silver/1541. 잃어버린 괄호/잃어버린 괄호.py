num = input().split('-')

result = []

for i in num:
    if '+' in i:
        plus = sum(list(map(int, i.split('+'))))
        result.append(plus)
    else:
        result.append(int(i))
        
a = result[0]       

for results in result[1:]:
    a -= results
    
print(a)