import sys
input = sys.stdin.readline

N = int(input())
data = [[] for _ in range(2)]
nxtA = 0
nxtB = 0

for i in range(N-1):
    A,B,AtoB,BtoA = map(int,input().split())
    if i == 0:                                  # 첫 수행
        data[0].append(A)
        data[1].append(B)
        nxtA = min(A,B+BtoA)                    # 다음 노드 A에 더할 값
        nxtB = min(B,A+AtoB)                    # 다음 노드 B에 더할 값
        # print(A,B+BtoA)
        # print(B,A+AtoB)
    else:
        A = A+nxtA                              # 현재 노드A + 더할 값 = 해당 노드 최소 누적 값
        B = B+nxtB
        data[0].append(A)
        data[1].append(B)
        nxtA = min(A,B+BtoA)                    # 다음 노드 A에 더할 값
        nxtB = min(B,A+AtoB)
        # print(A,B+BtoA)
        # print(B,A+AtoB)

A,B = map(int,input().split())                  # 마지막 수행
A = A+nxtA
B = B+nxtB
data[0].append(A)
data[1].append(B)
# print(data)
print(min(data[0][N-1],data[1][N-1]))
