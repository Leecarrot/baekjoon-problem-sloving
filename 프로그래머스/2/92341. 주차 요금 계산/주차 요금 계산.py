import math

def solution(fees, records):
    park = {}
    result = []
    for record in records:
        time, num, a = record.split()
        if num not in park:
            park[num] = [time]
        else:
            park[num].append(time)
            
    for i in park:
        if len(park[i]) % 2 != 0:
            park[i].append('23:59')
    
    park = dict(sorted(park.items(), key = lambda x:x[0]))
    
    for i in park:
        plus = 0
        for j in range(len(park[i]) - 1, 0, -2):
            a, b = park[i][j].split(':')
            c, d = park[i][j - 1].split(':')
            s = (int(a) * 60 + int(b)) - (int(c) * 60 + int(d)) 
            plus += s
        if plus > fees[0]:
            final = fees[1] + math.ceil(((plus - fees[0])/fees[2])) * fees[3]
            result.append(final)
        else:
            result.append(fees[1])
    return result