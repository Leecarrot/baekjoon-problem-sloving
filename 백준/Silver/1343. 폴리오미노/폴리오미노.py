import re

data = input()
pattern = re.compile(r'(X+|\.+)')
data = pattern.findall(data)

result = []
for i in data:
    if '.' in i:
        result.append(i)
    elif len(i) % 2 == 0:
        if len(i) >= 4:
            i = i.replace('XXXX', 'AAAA')
        if len(i) >= 2:
            i = i.replace('XX', 'BB')
            result.append(i)
    else:
        result.append(-1)

if -1 in result:
    print(-1)
else:
    for i in result:
        print(i, end = '')