import sys
input = sys.stdin.readline

K,P,N = map(int,input().split())

virus = K
for _ in range(N):
    virus = virus*P%1000000007

print(virus)