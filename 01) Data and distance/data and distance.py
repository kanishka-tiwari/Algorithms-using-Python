#data as a dictionary of connections

raw_input = input("Enter graph dictionary (example input: {"A": [["B", 5], ["C", 2]], "B": [["C", 1]], "C": []}): ")
graph = eval(raw_input)  

start_node = input("Enter starting node: ")
algorithm = input("Choose (dijkstra / bellman): ").strip().lower()

#track shortest distances

distances = {}
for node in graph:
    distances[node] = float('inf')
distances[start_node] = 0