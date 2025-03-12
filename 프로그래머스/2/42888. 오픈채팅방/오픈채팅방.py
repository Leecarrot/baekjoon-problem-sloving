def solution(record):
    result = []
    final = []
    uid = {}
    
    for i in record:
        a = i.split(' ')
        if a[0] == 'Enter':
            uid[a[1]] = a[2]
            result.append('{} 들어왔습니다.'.format(a[1]))
        elif a[0] == 'Leave':
            result.append('{} 나갔습니다.'.format(a[1]))
        else:
            uid[a[1]] = a[2]
            
    for i in result:
        a = i.split(' ')
        final.append(uid[a[0]] + '님이' + ' ' + a[1])
        
    return final