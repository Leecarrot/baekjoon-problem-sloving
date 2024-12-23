def solution(n, lost, reserve):
    answer = n - len(lost) + len(set(reserve) & set(lost))
    reserve_ = sorted(set(reserve) - set(lost))
    lost_ = sorted(set(lost) - set(reserve))
    
    for i in reserve_:
        if i - 1 in lost_:
            lost_.remove(i - 1)
            answer += 1
        elif i + 1 in lost_:
            lost_.remove(i + 1)
            answer += 1
    
    return answer    