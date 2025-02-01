def solution(clothes):
    
    cloth_dict = {}
    
    for i in clothes:
        if i[1] not in cloth_dict:
            cloth_dict[i[1]] = 2
        else:
            cloth_dict[i[1]] += 1
    
    do = 1
    
    for j in cloth_dict.values():
            do = do * j
            
    return do - 1

        