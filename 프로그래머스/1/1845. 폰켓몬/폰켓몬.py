def solution(nums):
    max_num = len(nums)//2
    
    if len(set(nums)) >= max_num:
        return max_num
    else:
        return len(set(nums))