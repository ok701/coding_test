import sys
input = sys.stdin.readline
sys.setrecursionlimit(10*4)
# import time

# s = time.time()
K,P,N = map(int,input().split())

# caculate K*P**(10*N)
 
def cal(p,n):
    if n == 1:
        return p
    if n%2 == 0:  # even
        v = cal(p,n/2)         
        return v*v%1000000007
    else:  # odd
        v = cal(p,n//2)         
        return v*v*p%1000000007

print(K*cal(P,10*N)%1000000007)