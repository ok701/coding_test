list = []

for a in range(10):
  for b in range(10):
    for c in range(10):
      for d in range(10):
        inv = 1001*a + 101*b + 11*c + 2*d
        list.append(inv)

list.sort()

for i in range(10000):
  if i not in list:
    print(i)