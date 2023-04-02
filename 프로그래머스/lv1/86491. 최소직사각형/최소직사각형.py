def solution(sizes):
    
    for i in sizes:
        i.sort()
    
    max1 = sizes[0][0]
    max2 = sizes[0][1]
    for i in sizes:
        if max1 < i[0]:
            max1 = i[0]
        if max2 < i[1]:
            max2 = i[1]

    answer = max1 * max2
    return answer