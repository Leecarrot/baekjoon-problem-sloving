def solution(sizes):
    result = 0
    a = []
    b = []
    for i in sizes:
        result = max(i[0], i[1], result)
    
    for i in sizes:
        if abs(result - i[0]) >= abs(result - i[1]):
            a.append(i[1])
            b.append(i[0])
        else:
            a.append(i[0])
            b.append(i[1])
    return max(a) * max(b)
        
        