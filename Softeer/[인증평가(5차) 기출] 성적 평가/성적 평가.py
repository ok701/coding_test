import sys
N = int(input())

table = []
for _ in range(3):
    table.append(list(map(int,sys.stdin.readline().split())))
table.append([table[0][i]+table[1][i]+table[2][i] for i in range(N)])

# print(table)

for i in range(4):
    temp = table[i][::]
    # print(temp)
    sorted_nodes = sorted(table[i], reverse=True)
    rank = {}
    r = 0
    pre_j = -1
    for j in sorted_nodes:
        if j != pre_j:
            r += 1
            rank[j] = r
            pre_j = j
        else:
            r += 1
            pre_j = j
    for k in range(N):
        print(rank[table[i][k]],end=' ')
    print()
