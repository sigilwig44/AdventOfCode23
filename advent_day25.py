import networkx as nx
import matplotlib.pyplot as plt

def read_connections(filename):
    connections = {}
    with open(filename, 'r') as f:
        for line in f:
            key, value = line.strip().split(': ')
            connections[key] = value.split(' ')
    return connections

def remove_connections(connections):
    for key, to_remove in [('fdb', 'txm'), ('nmz', 'mnl'), ('vgf', 'jpn')]:
        connections[key].remove(to_remove)
    return connections

def get_neighbors(graph, node):
    neighbors = set()
    for item in graph.get(node, []):
        neighbors.add(item)
    for key, value in graph.items():
        if node in value:
            neighbors.add(key)
    return list(neighbors)


def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(get_neighbors(graph, node))

    return len(visited)

connections = read_connections('day25_input.txt')
connections = remove_connections(connections)

print(dfs(connections, 'qpv') * dfs(connections, 'qbv'))

# create an empty graph
G = nx.Graph()

# add nodes and edges to the graph
for node, edges in connections.items():
    for edge in edges:
        G.add_edge(node, edge)

# draw the graph
nx.draw(G, with_labels=True)
plt.show()