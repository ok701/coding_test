def solution(nums):
    nums_type = len(set(nums))
    total = len(nums)/2
    
    answer = min(nums_type,total)
    return answer