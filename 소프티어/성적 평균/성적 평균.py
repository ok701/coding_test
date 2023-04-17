import sys

N,K = map(int,input().split())
# N:학생 수 K:구간 수

score = list(map(int,input().split()))

# print(score)

for _ in range(K):
    total_score = 0
    a,b = map(int,input().split())
    for i in range(a-1,b):
        total_score += score[i]
        # print(total_score)

    res = total_score/(b-a+1)
    print(f'{res:.2f}')