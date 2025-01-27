n = int(input())
final = []

for _ in range(n):
    a = int(input())
    part_list = list(map(int, input().split()))
    
    filtered_list = [i for i in part_list if part_list.count(i) == 6]
    
    score = [(i, j) for i, j in enumerate(filtered_list)]
    
    score_dic = {i: 0 for i in set(filtered_list)}
        
    for i in set(filtered_list):
        count = 0
        for j in score:
            if j[1] == i:
                count += 1
                score_dic[j[1]] += j[0]
                if count == 4:
                    break
    
    min_score = min(score_dic.values())
    
    team = 0
    min_team = []
    score_dic2 = {}
    
    for i in score_dic.keys():
        if score_dic[i] == min_score:
            team += 1
            min_team.append(i)
            
    if len(min_team) == 1:
        final.append(min_team[0])
    else:
        for i in min_team:
            count = 0
            for j in score:
                if j[1] == i:
                    count += 1
                    if count <= 5:
                        score_dic2[j[1]] = j[0]
                        
        min_score2 = min(score_dic2.values())
        for i in score_dic2.keys():
            if score_dic2[i] == min_score2:
                final.append(i)
                
for i in final:
    print(i)