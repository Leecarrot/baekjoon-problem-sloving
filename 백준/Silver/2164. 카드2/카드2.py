from collections import deque

n = int(input())

n_list = [i for i in range(1, n + 1)]

que = deque(n_list)

if n == 1:
    print(1)
else:
    while True:
        que.popleft()
        x = que.popleft()
    
        que.append(x)
    
        if len(que) == 1:
            break
        
    print(que[0])