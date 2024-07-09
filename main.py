"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def longest_path(graph: list) -> int:
    # Your implementation goes here
    # pass
    # Perform topological sort to get the order of nodes
    topo_order = topological_sort(graph)
    # Calculate and return the longest path using the topological order
    return calculate_longest_path(graph, topo_order)

# Helper function to perform topological sort
def topological_sort(graph):
    # Your implementation goes here
    # pass
    n = len(graph)
    in_degree = [0] * n
    for i in range(n):
        for j, w in graph[i]:
            in_degree[j] += 1

    # Use a queue to store nodes with in-degree of 0
    queue = [i for i in range(n) if in_degree[i] == 0]
    topo_order = []

    while queue:
        node = queue.pop(0)
        topo_order.append(node)
        for neighbor, weight in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return topo_order

# Function to calculate longest path using topological sort
def calculate_longest_path(graph, topo_order):
    # Your implementation goes here
    # pass
    n = len(graph)
    dist = [-float('inf')] * n

    # Initialize distances for nodes that can start a path
    for u in topo_order:
        if dist[u] == -float('inf'):
            dist[u] = 0  # Initialize the distance of the first occurrence

        for v, weight in graph[u]:
            if dist[u] + weight > dist[v]:
                dist[v] = dist[u] + weight

    # Return the maximum distance
    return max(dist)

# Example usage:
if __name__ == "__main__":

    graph1 = [
        [(1, 3), (2, 2)],
        [(3, 4)],
        [(3, 1)],
        []
    ]
    print(longest_path(graph1))  # Output: 7

    graph2 = [
        [(1, 2), (2, 1)],
        [(3, 1)],
        [(3, 5)],
        []
    ]
    print(longest_path(graph2))  # Output: 6

    graph3 = [
        [(1, 10)],
        [(2, 10)],
        [(3, 10)],
        []
    ]
    print(longest_path(graph3))  # Output: 30

    graph4 = [
        [(1, 1), (2, 1)],
        [(3, 1)],
        [(3, 1)],
        []
    ]
    print(longest_path(graph4))  # Output: 2 Given Output is wrong
