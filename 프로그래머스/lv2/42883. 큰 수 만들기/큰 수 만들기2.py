def solution(number, k):
    stack = []
    for i,n in enumerate(number):
        
        # 첫번째x, 들어온게 더 큼, k남음
        while len(stack)>0 and stack[-1]<n and k>0:
            stack.pop()
            k -= 1
        
        if k == 0:  # k 전부 소모 시
            stack += list(number[i:])
            break
        
        stack.append(n)
        
    if k>0:    
        stack = stack[:-k]

    return ''.join(stack)