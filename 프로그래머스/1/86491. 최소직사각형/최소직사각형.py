def solution(sizes):
    a = []
    b = []
    
    for i in sizes:
        a.append(max(i[0], i[1]))
        b.append(min(i[0], i[1]))
    
    return max(a) * max(b)
        