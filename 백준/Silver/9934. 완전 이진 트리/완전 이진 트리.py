K = int(input())  # K줄

Nodes = list(map(int,input().split()))

tree = list([] for _ in range(K))
depth = 0

def dfs(nodes,depth):
  
  mid = len(nodes)//2
  #print(nodes)
  #print(mid)
  
  tree[depth].append(nodes[mid])
  #print(tree)
  
  if len(nodes) == 1:
    return

  dfs(nodes[:mid],depth+1)
  dfs(nodes[mid+1:],depth+1)


dfs(Nodes,0)

for i in tree:
  print(*i)
