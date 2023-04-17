def solution(phone_book):
    phone_book.sort()
    res = True
    if len(phone_book) == 1:
        res = True
    for i in range(len(phone_book)-1):
        pre = phone_book[i]
        comp = phone_book[i+1]
        if comp.startswith(pre):
            res = False
            break

    return res