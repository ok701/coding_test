def solution(participant, completion):
    
    ppl = {}
    for p in participant:
        ppl[p] = ppl.get(p,0) + 1
        
    for c in completion:
        ppl[c] -= 1   
        
    for k,v in ppl.items():
        if v != 0:
            res = k
    return res