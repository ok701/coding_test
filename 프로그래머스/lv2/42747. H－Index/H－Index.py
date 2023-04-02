def solution(citations):
    citations.sort(reverse = True)
    
    for idx,v in enumerate(citations):
        if citations[0] == 0:
            return 0
        if idx+1 > v:
            return idx
        if idx+1 == v:
            return idx+1
        
    return idx+1