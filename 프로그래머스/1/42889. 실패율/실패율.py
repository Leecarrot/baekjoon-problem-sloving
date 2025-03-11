def solution(N, stages):
    n = {}
    
    for i in range(1, N + 1):
        n[i] = 0
    
    pp = len(stages)
    
    for i in range(1, N + 1):
        if pp > 0:
            n[i] = stages.count(i) / pp
            pp -= stages.count(i)
    
    
    result = [key for key, value in sorted(n.items(), key=lambda item: (item[1], -item[0]), reverse=True)]
    
    return result