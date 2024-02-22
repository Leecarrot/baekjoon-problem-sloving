for _ in range(int(input())):
    result = []
    
    for _ in range(int(input())):
        a, b = input().split()
        result.append((int(a), int(b)))
        
    result_sort = sorted(result)
        
    count = 1
    min_num = result_sort[0][1]
    
    for i in result_sort[1:]:
        if i[1] < min_num:
            count += 1
            min_num = i[1]
    
    print(count)