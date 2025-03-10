def solution(board, moves):
    stack = []
    result = 0
    
    for move in moves:
        for x in range(len(board)):
            if board[x][move - 1] != 0:
                if stack and stack[-1] == board[x][move - 1]:
                    stack.pop()
                    result += 2
                else:
                    stack.append(board[x][move - 1])
                board[x][move - 1] = 0
                break
    return result
        