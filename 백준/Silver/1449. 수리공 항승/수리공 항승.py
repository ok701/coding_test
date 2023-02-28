N,L = map(int,input().split())
nodes = list(map(int,input().split()))
nodes.sort()

cnt = 0
last_tape = 0

for node in nodes:
  if node > last_tape:
    cnt += 1
    last_tape = node + (L-1)

print(cnt)