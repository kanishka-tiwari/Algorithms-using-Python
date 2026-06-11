#Dijkstra's algorithm (using list)

if algorithm == "dijkstra":
    unvisited = list(graph.keys())
    
    while unvisited:
        current_node = unvisited[0]
        for node in unvisited:
            if distances[node] < distances[current_node]:
                current_node = node
                
        unvisited.remove(current_node)
        
        for edge in graph[current_node]:
            neighbor = edge[0]
            weight = edge[1]
            
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance 