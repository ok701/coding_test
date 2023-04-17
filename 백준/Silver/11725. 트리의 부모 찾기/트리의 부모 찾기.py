import sys
sys.setrecursionlimit(10 ** 6)
    
N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
  a,b = map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

# print(graph)

visited = [False for _ in range(N+1)]
res = [0 for _ in range(N+1)]

def dfs(s): 
  visited[s] = True
  for adj in sorted(graph[s]):
     if not visited[adj]:
        res[adj] = s
        dfs(adj)

dfs(1)

for i in range(2,N+1):
  print(res[i])