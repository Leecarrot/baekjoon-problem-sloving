n = input()
num = 0
idx = 0

while True:
    num += 1
    for i in str(num):
        if n[idx] == i:
            idx += 1
            if idx == len(n):
                print(num)
                break
        if idx == len(n):
            break
    if idx == len(n):
        break