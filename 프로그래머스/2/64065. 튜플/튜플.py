def solution(s):
    result = []
    
    s = s[2:-2]
    str_groups = s.split("},{")
    
    s1 = [list(map(int, group.split(','))) for group in str_groups]
    
    s2 = sorted(s1, key = lambda x:len(x))
    
    for i in s2:
        for j in i:
                if j not in result:
                    result.append(j)
    return result