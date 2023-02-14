N = int(input())
links = list(map(int,input().split()))
nodes = list(map(int,input().split()))

links.append(0)  # 2 3 1 0
nodes[-1] = 0    # 5 2 4 0

pre_node = nodes[0]
ext_links = links[0]
cost = 0

for i in range(1,N):
  if(nodes[i]<pre_node):
    cost += pre_node*ext_links
    pre_node = nodes[i]
    ext_links = links[i]
  else:
    ext_links += links[i]

print(cost)