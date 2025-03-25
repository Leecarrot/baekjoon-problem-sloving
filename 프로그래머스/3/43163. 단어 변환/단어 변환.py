from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    que = deque([(begin, 0)])
    visited = set()
    
    while que:
        word, count = que.popleft()
        
        if word == target:
            return count
        
        for index in range(len(words)):
            plus = 0
            for i, j in zip(word, words[index]):
                if i != j:
                    plus += 1
                    
            if plus == 1 and words[index] not in visited:
                que.append((words[index], count + 1))
                visited.add(words[index])
    
    return 0
            
            