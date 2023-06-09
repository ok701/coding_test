# def solution(participant, completion):
    
#     dic = {}
#     for a in participant:
#         dic[a] = 0

#     for a in participant:
#         dic[a] += 1

    
#     for a in completion:
#         dic[a] -= 1
        
#     for i in dic:
#         if dic[i] != 0:
#              answer = i
             
  
#     return answer

from collections import Counter

def solution(participant, completion):
    return ''.join(Counter(participant) - Counter(completion))