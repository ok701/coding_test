from collections import deque

# nodes_ = 4
# lines_ = 5
# start = 1

nodes_, lines_, start = map(int, input().split())

# lines = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]

lines = []
for i in range(lines_):
  lines.append(list(map(int,input().split())))
  

graph = [[] for i in range(nodes_ + 1)]

for i in range(lines_):
  graph[lines[i][0]].append(lines[i][1])
  graph[lines[i][1]].append(lines[i][0])

for row in graph:
  row.sort()

# print('graph : ', graph)


# DFS
def dfs(graph, k, visited):
  visited[k] = True
  print(k, end=' ')
  for node_adj in graph[k]:
    if not visited[node_adj]:
      dfs(graph, node_adj, visited)


# BFS
def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    node = queue.popleft()
    print(node, end=' ')
    for node_adj in graph[node]:
      if not visited[node_adj]:
        queue.append(node_adj)
        visited[node_adj] = True


visited = [False] * (nodes_ + 1)
# print('visited : ', visited)
dfs(graph, start, visited)
print()
visited = [False] * (nodes_ + 1)
bfs(graph, start, visited)
