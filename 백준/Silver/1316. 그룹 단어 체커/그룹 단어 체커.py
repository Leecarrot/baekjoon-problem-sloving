count = 0

for _ in range(int(input())):
    word = input()
    pre = ''
    seen = set()
    is_group = True
    
    
    for char in word:
        if char != pre:
            if char in seen:
                is_group = False
                break
            seen.add(char)
        pre = char
    
    if is_group:
        count += 1
        
print(count)