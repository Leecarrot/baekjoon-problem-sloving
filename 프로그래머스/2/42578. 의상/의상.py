def solution(clothes):
    style = {}
    
    # 옷 종류별로 딕셔너리에 모으기
    for cloth_name, cloth_type in clothes:
        if cloth_type not in style:
            style[cloth_type] = [cloth_name]
        else:
            style[cloth_type].append(cloth_name)
    
    # 조합 경우 수 계산
    count = 1
    for items in style.values():
        count *= (len(items) + 1)  # 안 입는 경우 포함
    
    return count - 1  # 모두 안 입는 경우 제외