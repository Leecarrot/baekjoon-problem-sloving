def solution(participant, completion):
    pa_dic = {}
    final = participant + completion
    
    for i in final:
        if i not in pa_dic:
            pa_dic[i] = 1
        else:
            pa_dic[i] += 1
    
    for i in pa_dic.keys():
        if pa_dic[i] % 2 != 0:
            return i
        
    
    
        
    
    
    
    