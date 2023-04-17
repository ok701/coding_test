import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    n, wtk = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))
    que = [(i, li[i]) for i in range(len(li))]
    print(li)
    print(que)
    li.sort(reverse=True)
    print(li)
    k = 0
    for el in li:
        while que[0][1] != el:
            tmp = que.pop(0)
            que.append(tmp)
        k += 1
        if que.pop(0)[0] == wtk:
            break
    print(k)
