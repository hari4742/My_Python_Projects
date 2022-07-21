from graphs import sample_graph
n = 13  # number of nodes
graph = sample_graph

# global visited list
visited = [False] * n


def dfs(node):
    if visited[node]:
        return
    visited[node] = True
    print(node, end=" ")
    for next_node in graph[node]:
        dfs(next_node)


for node in range(n):
    dfs(node)
