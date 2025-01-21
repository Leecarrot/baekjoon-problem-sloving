def solution(participant, completion):
    pa_dic = {}
    
    for i in participant:
        if i not in pa_dic:
            pa_dic[i] = 1
        else:
            pa_dic[i] += 1
    
    for i in completion:
        pa_dic[i] -= 1
    
    for i in pa_dic:
        if pa_dic[i] == 1:
            return i