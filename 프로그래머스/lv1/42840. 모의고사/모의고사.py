def solution(answers):
    N = len(answers)
    
    # student1
    pattern = [1,2,3,4,5] 
    student1 = pattern * (N // 5) + pattern[:N%5]  
        
    # student2
    pattern = [2,1,2,3,2,4,2,5] 
    student2 = pattern * (N // 8) + pattern[:N%8]

    # student3
    pattern = [3,3,1,1,2,2,4,4,5,5] 
    student3 = pattern * (N // 10) + pattern[:N%10]
    
    cnt = [0,0,0]
    for i in range(N):
        if answers[i] == student1[i]:
            cnt[0] += 1
        if answers[i] == student2[i]:
            cnt[1] += 1
        if answers[i] == student3[i]:
            cnt[2] += 1
    
    res = []
    max_ = 0
    for i in range(len(cnt)):
        if cnt[i] > max_:
            res = []
            res.append(i+1)
            max_ = cnt[i]
        if cnt[i] == max_:
            res.append(i+1)

    return list(set(sorted(res)))