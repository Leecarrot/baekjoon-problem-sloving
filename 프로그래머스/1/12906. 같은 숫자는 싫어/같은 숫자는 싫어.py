from collections import deque

def solution(arr):
    answer = []
    que = deque(arr)
    
    for i in range(len(arr)):
        a = que.popleft()
        if que and a != que[0]:
            answer.append(a)
    answer.append(arr[-1])
            
    return answer