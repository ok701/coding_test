def solution(n, lost, reserve):
    
    L = set(lost)-set(reserve)  # 겹치는 것은 제외
    R = set(reserve)-set(lost)
    # print(l,r)

    for r in sorted(R):
        if r-1 in L:
            L.remove(r-1)
        elif r+1 in L:
            L.remove(r+1)
            
    return n-len(L)