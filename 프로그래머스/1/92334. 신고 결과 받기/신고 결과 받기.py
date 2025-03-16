def solution(id_list, report, k):
    goal = {i:0 for i in id_list}
    real = {i:[] for i in id_list}
    
    for i in set(report):
        a, b = i.split()
        real[a].append(b)
        goal[b] += 1

    result = []
    
    for i in real:
        count = 0
        for j in real[i]:
            if goal[j] >= k:
                count += 1
        result.append(count)
    return result
        