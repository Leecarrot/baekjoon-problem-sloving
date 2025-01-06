def solution(name):
    n = len(name)
    answer = 0
    move = n - 1

    # 알파벳 변경 횟수 계산
    for i in range(n):
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        
        next_pos = i + 1
        while next_pos < n and name[next_pos] == 'A':
            next_pos += 1
            
        move = min(move, i + n - next_pos + min(i, n - next_pos))
    
    answer += move
    return answer