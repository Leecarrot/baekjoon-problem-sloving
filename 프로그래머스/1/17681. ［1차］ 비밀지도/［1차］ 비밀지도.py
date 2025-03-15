def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        row = bin(arr1[i] | arr2[i])[2:].zfill(n)  # OR 연산 후 이진수 변환
        # '1'은 벽(#), '0'은 공백( )으로 바꿔서 리스트에 추가
        row = row.replace('1', '#').replace('0', ' ')
        answer.append(row)
    
    return answer