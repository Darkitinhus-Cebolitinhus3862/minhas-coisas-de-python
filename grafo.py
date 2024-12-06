#Christian Kennedy Daniel Martins GRR20221099

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 7},
    'B': {'A': 4, 'C': 1, 'E': 1},
    'C': {'A': 2, 'B': 1, 'D': 3, 'E': 3},
    'D': {'A': 7, 'C': 3, 'E': 2},
    'E': {'B': 1, 'C': 3, 'D': 2}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  
    previous_nodes = {node: None for node in graph}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

def reconstruct_path(previous_nodes, start, end):
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]
    return path if path[0] == start else None

distances, previous_nodes = dijkstra(graph, 'A')

time_to_E = distances['E']
path_to_E = reconstruct_path(previous_nodes, 'A', 'E')

time_to_D = distances['D']
path_to_D = reconstruct_path(previous_nodes, 'A', 'D')

print(f"Menor tempo de A até E: {time_to_E} horas")
print(f"Caminho: {' -> '.join(path_to_E)}")
print(f"Menor tempo de A até D: {time_to_D} horas")
print(f"Caminho: {' -> '.join(path_to_D)}")
