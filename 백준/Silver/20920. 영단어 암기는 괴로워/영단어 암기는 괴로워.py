import sys
input=sys.stdin.readline

n, m = map(int, input().split())

words_dic = {}

for _ in range(n):
    wo = input().strip()
    if len(wo) >= m:
        if wo not in words_dic.keys():
            words_dic[wo] = 1
        else:
            words_dic[wo] += 1

sorted_dict = dict(sorted(words_dic.items(), key=lambda item: (-item[1], -len(item[0]), item[0])))

for j in sorted_dict:
    print(j)