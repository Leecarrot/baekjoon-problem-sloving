from collections import deque

def solution(priorities, location):
    max_num = max(priorities)
    que = deque()
    prio_list = priorities[:]
    
    for i, j in enumerate(priorities):
        que.append((i, j))
    
    count = 0
    while que:
        
        i, j = que.popleft()
        
        if j < max_num:
            que.append((i, j))

        else:
            count += 1
            prio_list.remove(j)
            if location == i:
                return count 
            
            if prio_list:
                max_num = max(prio_list)
    
    
    
    
        
    