from collections import deque

def solution(progresses, speeds):
    
    final = []
    que = deque(progresses)
    speeds = deque(speeds)
    
    while que:
        # speeds만큼 더하는 코드
        for i in range(len(que)):
            que[i] += speeds[i]
            
        count = 0
        while que and que[0] >= 100:
            que.popleft()
            speeds.popleft()
            count += 1
            
        if count > 0:
            final.append(count)
        
    return final
            
            
    
    