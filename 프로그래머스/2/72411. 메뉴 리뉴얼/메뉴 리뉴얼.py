from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []
    
    for num in course:
        possible_combinations = []
        
        for order in orders:
            sorted_order = sorted(order)
            comb = combinations(sorted_order, num)  # 조합 생성
            possible_combinations += comb  # 모든 조합 추가
        
        comb_counter = Counter(possible_combinations)  # 빈도수 계산
        if not comb_counter:
            continue  # 해당 course 크기의 조합이 없으면 넘어감

        max_count = max(comb_counter.values())  # 가장 많이 주문된 횟수 찾기

        # 최소 2번 이상 주문된 조합만 결과에 추가
        if max_count >= 2:
            for key, val in comb_counter.items():
                if val == max_count:
                    result.append("".join(key))

    return sorted(result)  # 결과 정렬 후 반환
