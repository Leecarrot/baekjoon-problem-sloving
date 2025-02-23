
def solution(plans):
    stack = []
    answer = []
    
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h*60 + m
        plans[i][2] = int(plans[i][2])
        
    plans.sort(key=lambda x: x[1])
    
    for i in range(len(plans)-1):
        stack.append([plans[i][0], plans[i][2]])
        gap = plans[i+1][1] - plans[i][1]
        
        while stack and gap:
            if stack[-1][1] <= gap:
                cn, ct = stack.pop()
                gap -= ct
                answer.append(cn)
            else:
                stack[-1][1] -= gap
                gap = 0
    answer.append(plans[-1][0])
    for i in range(len(stack)):
        answer.append(stack[~i][0])
    return answer