def solution(number, k):
    l = len(number)
    stack = [9]
    i = 0
    while(True):
        if i == l:
            for i in range(k):
                stack.pop()
            print(stack)
            break
            
        if k == 0:
            for v in number[i:]:
                stack.append(int(v))    
            break

        elif stack[-1] >= int(number[i]):
            stack.append(int(number[i]))
            i += 1

        else:
            stack.pop()
            k -= 1    

    answer = ''.join(str(s) for s in stack[1:])
    return answer