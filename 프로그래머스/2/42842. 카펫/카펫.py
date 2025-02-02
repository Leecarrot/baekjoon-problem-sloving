def solution(brown, yellow):
    by = brown + yellow
    
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            if ((yellow // i) + 2) * (i + 2) == by:
                d = [(yellow // i) + 2, i + 2]
                final = sorted(d, reverse = True)
                return final
            