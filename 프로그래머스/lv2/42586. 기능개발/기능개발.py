import math
from collections import Counter

days= []
def solution(progresses, speeds):
    
    for i in range(len(progresses)):
        left = 100 - progresses[i]
        if i == 0 or left / speeds[i] > days[-1]:
            days.append(math.ceil(left / speeds[i]))
        else:
            days.append(days[-1])

    answer = list(Counter(days).values())
    return answer