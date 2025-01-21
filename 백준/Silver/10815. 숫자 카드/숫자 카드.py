n = int(input())
n_dict = {}
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

for i in n_list:
    n_dict[i] = 1

for j in m_list:
    if j in n_dict:
        print(1, end = ' ')
    else:
        print(0, end = ' ')