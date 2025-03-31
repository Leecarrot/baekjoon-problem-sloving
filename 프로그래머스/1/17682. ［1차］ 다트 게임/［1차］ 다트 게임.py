def solution(dartResult):
    import re
    
    # 정규식을 이용해 각 점수 블록을 분리 (점수+보너스+옵션까지)
    rounds = re.findall(r'(\d+)([SDT])([*#]?)', dartResult)
    
    scores = []
    bonus = {'S': 1, 'D': 2, 'T': 3}

    for i, (num, b, option) in enumerate(rounds):
        score = int(num) ** bonus[b]  # 점수 계산
        
        if option == '*':  # 스타상 (*)
            score *= 2
            if i > 0:  # 이전 점수도 2배
                scores[i - 1] *= 2
        elif option == '#':  # 아차상 (#)
            score *= -1

        scores.append(score)

    return sum(scores)