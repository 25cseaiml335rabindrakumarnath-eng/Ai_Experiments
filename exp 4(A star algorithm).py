Experiment-04

1. WAP for A* Algorithm.

THEORY:

* It is a path finding algorithm that finds the shortest
  and the most efficient path from a start node to a
  goal node by using:

. g(x) = Actual cost from the start node to node (x)
. h(x) = Estimated cost from node (x) to the goal.
. f(x) = Estimated total cost of the path.

             f(x) = g(x) + h(x)

        Total estimated cost
        Actual cost so far
        Estimated remaining cost

A* search algorithm is an informed search algorithm,
that finds the shortest path by combining the actual
cost from the start node and the estimated cost to the
goal.
A* algorithm:

def a_star(graph, heuristic, start, goal):
    open_list = [start]
    closed_list = []

    #g-cost = cost from start node
    g_cost = {start: 0}

    # Parent dictionary to reconstruct the path,
    parent = {start: None}

    while open_list:
        # Select node having minimum f(n) = g(n) + h(n)
        current = open_list[0]

        for node in open_list:
            f-current = g-cost[current] + heuristic[current]
            f-node = g-cost[node] + heuristic[node]

            if f-node < f-current:
                current = node

        # Goal reached
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            print("\nShortest Path:", "->".join(path))
            print("Total Cost:", g-cost[goal])
            return

        open_list.remove(current)
        closed_list.append(current)
# Check all neighboring nodes
for neighbor, cost in graph[current]:
    if neighbor in closed_list:
        continue

    new-cost = g-cost[current] + cost

    # If neighbor is new or a better path is found
    if neighbor not in open_list or new-cost < g-cost.get(
        neighbor, float('inf')):

        g-cost[neighbor] = new-cost
        parent[neighbor] = current

        if neighbor not in open_list:
            open_list.append(neighbor)

print("\nNo path found.")

# ---------------- USER INPUT ----------------

graph = {}

n = int(input("Enter number of nodes:"))

print("\nEnter node names:")
nodes = []

for i in range(n):
    node = input(f"Node {i+1}:")
    nodes.append(node)
    graph[node] = []

# Enter edges
e = int(input("\nEnter number of edges:"))

print("\nEnter edges in the following format:")
print("Source Destination Cost")
for i in range(e):
    source = input(f"\nEdge {i+1} source:")
    destination = input(f"Edge {i+1} destination:")
    cost = int(input("Cost:"))

    graph[source].append((destination, cost))

# Enter heuristic values
heuristic = {}

print("\nEnter heuristic values h(n):")

for node in nodes:
    heuristic[node] = int(input(f"h({node}):"))

# Start and goal
start = input("\nEnter start node:")
goal = input("Enter goal node:")

# Run A* Algorithm
a_star(graph, heuristic, start, goal)
