# Algorithms-using-Python
Demonstrating Dijkstra's algorithm (using list) and Bellman-Ford algorithm (standard loops)

This code deals with a scenario where user has a graph dictionary and wants to fetch the quickest route from one node to another.

We can use any of the two algorithms for this and we offer this choice to the user.

Case 1) If user chooses Dijkstra's algorithm then we start by setting all initial distances to infinity, and start node to 0. We find the unvisited node with the smallest current distance, remove it from the unvisited list and update distances to all its neighbours.

Case 2) If user chooses Bellman-Ford algorithm then we start by setting all initial distances to infinity and running the relaxation process (Total Nodes - 1) times.
