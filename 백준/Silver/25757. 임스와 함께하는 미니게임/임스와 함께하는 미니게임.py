n, y = input().split()
name_list = []

for _ in range(int(n)):
    name_list.append(input())

name_set = set(name_list)

if y == 'Y':
    print(len(name_set))
    
elif y == 'F':
    print(len(name_set) // 2)
    
elif y == 'O':
    print(len(name_set) // 3)