def solution(array, commands):
    res = []
    for i in commands:
        slice = array[int(i[0])-1:int(i[1])]
        n = sorted(slice)[i[2]-1]
        res.append(n)
    return res