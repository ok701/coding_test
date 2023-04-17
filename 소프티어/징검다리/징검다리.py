import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

# print(N,A)

Lst_cnt = [1 for _ in range(N)]
# print(Lst_cnt)

for i in range(N):  # 기준점
    loc_max = 0
    for j in range(i):  # 그전 노드들 비교
        if A[i] > A[j]:
            loc_max = max(Lst_cnt[j],loc_max)
            # print('l_m:',loc_max)
    Lst_cnt[i] += loc_max
print(max(Lst_cnt))