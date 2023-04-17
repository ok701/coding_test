import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n,m = map(int,input().split())  # n:node m:link

adj = [[] for _ in range(n+1)]
adjR = [[] for _ in range(n+1)]
for i in range(m):
    i,j = map(int,input().split())
    adj[i].append(j)
    adjR[j].append(i)
s,t = map(int,input().split())


# print('n,m:',n,m)
# print('adj:',adj)
# print('adjR:',adjR)
# print('s,t:',s,t)

def dfs(now, adj, visit):
    if visit[now] == 1:
        return
    visit[now] = 1
    for now in adj[now]:
        dfs(now, adj, visit)

# S -> T
fromS = [0]*(n+1)
fromS[t] = 1
dfs(s,adj,fromS)

toT = [0]*(n+1)
dfs(t,adjR,toT)

# T -> S
fromT = [0]*(n+1)
fromT[s] = 1
dfs(t,adj,fromT)

toS = [0]*(n+1)
dfs(s,adjR,toS)

# print('fromS:',fromS)
# print('toT:',toT)

cnt = 0
for i in range(n+1):
    if fromS[i] == 1 and toT[i] == 1 and fromT[i] == 1 and toS[i] == 1:
        # print(i)
        cnt += 1

print(cnt-2)