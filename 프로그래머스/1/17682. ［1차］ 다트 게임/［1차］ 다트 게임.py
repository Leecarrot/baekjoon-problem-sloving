def solution(dartResult):
    final = []  # 점수를 저장할 리스트
    li = {'S': 1, 'D': 2, 'T': 3}  # 보너스 제곱 값
    
    result = ''  # 숫자를 담을 문자열
    
    for i in dartResult:
        if i.isdigit():
            result += i  # 숫자 이어붙이기 (10 처리 가능)
        elif i in li:
            final.append(int(result) ** li[i])  # 점수 계산 후 저장
            result = ''  # 숫자 초기화
        elif i == '*':
            # 현재 점수와 이전 점수를 2배 적용
            if final:
                final[-1] *= 2
            if len(final) > 1:
                final[-2] *= 2
        elif i == '#':
            final[-1] *= -1  # 바로 앞 점수를 음수로 변환
    
    return sum(final)  # 최종 점수 계산