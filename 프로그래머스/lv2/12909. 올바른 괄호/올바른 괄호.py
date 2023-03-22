def solution(s):
    res = True
    stack = []
    cnt = 0
    len_s = len(s)
    for i in s:
        cnt += 1
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                res = False
            else: 
                stack.pop()
        if cnt == len_s:
            if len(stack) != 0:
                res = False

    return res