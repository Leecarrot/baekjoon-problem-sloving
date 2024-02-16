n = int(input())
num_list = list(map(int, input().split()))
num = list(set(num_list))
num.sort()

num_dict = {}
result = 0


for i in num:
    num_dict[i] = result
    result += 1

for j in num_list:
    print(num_dict[j], end = ' ')