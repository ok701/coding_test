from collections import deque
res = []

def solution(arr):
    arrD = deque(arr)
    a = arrD.popleft()
    res.append(a)
    
    for _ in range(len(arr)-1):
        a = arrD.popleft()
        if a != res[-1]:
            res.append(a)
    answer = res
    return answer