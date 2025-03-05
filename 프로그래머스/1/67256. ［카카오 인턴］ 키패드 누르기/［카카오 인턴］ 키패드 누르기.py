def solution(numbers, hand):
    phone = {1:(0, 0), 2:(0, 1), 3:(0, 2), 
            4:(1, 0), 5:(1, 1), 6:(1, 2),
            7:(2, 0), 8:(2, 1), 9:(2, 2),
            0:(3, 1)}
    result = ''
    rnum = [3, 6, 9]
    lnum = [1, 4, 7]
    
    rd = (3, 2)
    ld = (3, 0)
    
    def manhattan_distance(pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    for num in numbers:
        if num in rnum:
            result += 'R'
            rd = phone[num]
        elif num in lnum:
            result += 'L'
            ld = phone[num]
        else:
            if manhattan_distance(phone[num], rd) > manhattan_distance(phone[num], ld):
                result += 'L'
                ld = phone[num]
            elif manhattan_distance(phone[num], rd) < manhattan_distance(phone[num], ld):
                result += 'R'
                rd = phone[num]
            else:
                if hand == 'right':
                    result += 'R'
                    rd = phone[num]
                else:
                    result += 'L'
                    ld = phone[num]
    return result
                                                                             
                                                                                                 
                        
                        
            