import heapq

def link_state_routing(graph, source):
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    pq = [(0, source)]  # (cost, node)

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, cost in graph[node]:
            if dist[neighbor] > dist[node] + cost:
                dist[neighbor] = dist[node] + cost
                heapq.heappush(pq, (dist[node] + cost, neighbor))
    return dist

# Example graph as adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

source = 'A'
print(link_state_routing(graph, source))
