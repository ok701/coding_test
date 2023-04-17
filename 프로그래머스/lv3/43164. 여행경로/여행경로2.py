def solution(tickets):

	graph = {}
	for t in tickets:
		graph[t[0]] = graph.get(t[0],[]) + [t[1]]
    
		for g in graph:
			graph[g].sort(reverse=True)
	stack = ["ICN"]
	rev_path = []
	
	while len(stack>0):
		top = stack[-1]
		if top not in graph or len(graph[top]) == 0:
			rev_path.append(stack.pop())
		else:
			stack.append(graph[top][-1])
			graph[top] = graph[top][:-1]
	return rev_path[::-1]