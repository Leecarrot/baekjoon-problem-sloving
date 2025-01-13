import sys
input=sys.stdin.readline

n = int(input())
a_dic = list(map(int, input().split()))
m = int(input())
b_dic = list(map(int, input().split()))
a_dic.sort()

for i in b_dic:
    if i in a_dic:
        print(1)
    else:
        print(0)