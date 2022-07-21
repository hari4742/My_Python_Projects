# find connected components of a graph using dfs
from graphs import connected_components_graph

# number of nodes
n = 18
# adjacency list of the graph
graph = connected_components_graph

visited = [False] * n

connected_components = 0
components = [0] * n


def dfs(node):
    if visited[node]:
        return
    visited[node] = True
    components[node] = connected_components
    for next_node in graph[node]:
        dfs(next_node)


for node in range(n):
    if not (visited[node]):
        connected_components += 1
        dfs(node)
print(connected_components)
print(components)
