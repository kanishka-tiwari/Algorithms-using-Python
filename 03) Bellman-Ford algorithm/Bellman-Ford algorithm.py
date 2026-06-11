#Bellman-Ford algorithm (standard loops)

elif algorithm == "bellman":
    for _ in range(len(graph) - 1):
        for current_node in graph:
            for edge in graph[current_node]:
                neighbor = edge[0]
                weight = edge[1]
                
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance