import sys

def distance_vector_routing(graph, source):
    # Initialize distance table
    dist = {node: sys.maxsize for node in graph}
    dist[source] = 0
    update = True
    while update:
        update = False
        for node in graph:
            for neighbor, cost in graph[node]:
                if dist[neighbor] > dist[node] + cost:
                    dist[neighbor] = dist[node] + cost
                    update = True
    return dist

# Example graph represented as an adjacency list (node -> [(neighbor, cost)])
graph = {
    'A': [('B', 1), ('C', 5)],
    'B': [('A', 1), ('C', 2)],
    'C': [('A', 5), ('B', 2)]
}

source = 'A'
print(distance_vector_routing(graph, "A"))
print(distance_vector_routing(graph, "B"))
print(distance_vector_routing(graph, "C"))
