from collections import deque

def solution(queue1, queue2):
    # 목표값 계산
    goal = (sum(queue1) + sum(queue2)) // 2
    
    # 두 큐를 deque로 변환
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    # 큐의 합을 계산하고 목표값을 만들 때까지 반복
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    result = 0
    max_operations = len(queue1) * 4  # 큐 크기 제한을 넘어가지 않도록
    
    while sum1 != goal:
        # 너무 많은 작업을 하지 않도록 제한을 둡니다
        if result >= max_operations:
            return -1
        
        if sum1 < goal:
            # queue2에서 원소를 꺼내 queue1에 추가
            val = queue2.popleft()
            queue1.append(val)
            sum1 += val
            sum2 -= val
            result += 1
        elif sum1 > goal:
            # queue1에서 원소를 꺼내 queue2에 추가
            val = queue1.popleft()
            queue2.append(val)
            sum1 -= val
            sum2 += val
            result += 1

        # 목표값에 도달했는지 체크
        if sum1 == goal:
            return result
    
    return result
    