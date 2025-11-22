def solution(ingredient):
    stack = []
    answer = 0
    
    for x in ingredient:
        stack.append(x)
        
        if len(stack) >= 4:
            if stack[-4:] == [1, 2, 3, 1]:
                # 4개 제거
                for _ in range(4):
                    stack.pop()
                answer += 1
                
    return answer
        