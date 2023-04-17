def solution(numbers):
    answer = ''
    numbers.sort(reverse=True, key = lambda x : str(x)*3)
    answer = ''.join(map(str,numbers))
    answer = answer+'#'

    for i in answer:
        if i == '#':
            return "0"
        if i != "0":
            break

    return answer[:-1]