import sys
sys.setrecursionlimit(10**6)

def solution(tickets):
        
    graph = {}
    for t in tickets:
        graph[t[0]] = graph.get(t[0],[]) + [t[1]]
    
    for i,v in graph.items():
        v.sort()
    print('graph',graph)

    stack = ["ICN"]
    rev_path = []
    def dfs(n):
        if n in graph and len(graph[n])>0:
                first_g = graph[n].pop(0)
                stack.append(first_g)
                dfs(first_g)
        else:
            if len(stack)>0:
                last_s = stack.pop()
                rev_path.append(last_s)
                print(rev_path)
                if len(stack)>0:
                    dfs(stack[-1])
            else:
                return
                
    dfs('ICN')           
    return rev_path[::-1]