# graph provides functions to create and manipulate graphs, including adding nodes, edges, and calculating shortest paths.

from collections import defaultdict, deque  
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_node(self, node):
        """Add a node to the graph."""
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        """Add an edge between two nodes."""
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def bfs(self, start):
        """Perform BFS traversal from a starting node."""
        visited = set()
        queue = deque([start])
        traversal_order = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                traversal_order.append(node)
                queue.extend(neighbor for neighbor in self.graph[node] if neighbor not in visited)

        return traversal_order

    def shortest_path(self, start, end):
        """Find the shortest path between two nodes using BFS."""
        if start == end:
            return [start]

        visited = {start}
        queue = deque([(start, [start])])

        while queue:
            current_node, path = queue.popleft()

            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [neighbor]
                    if neighbor == end:
                        return new_path
                    queue.append((neighbor, new_path))

        return None  # No path found

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    g.add_edge('D', 'E')                            
    print("BFS Traversal from A:", g.bfs('A'))
    print("Shortest path from A to E:", g.shortest_path('A', 'E'))
    print("Shortest path from B to C:", g.shortest_path('B', 'C'))
    print("Shortest path from C to D:", g.shortest_path('C', 'D'))
    print("Shortest path from E to A:", g.shortest_path('E', 'A'))
    print("Shortest path from A to A:", g.shortest_path('A', 'A'))
    print("Shortest path from B to E:", g.shortest_path('B', 'E'))
    print("Shortest path from D to C:", g.shortest_path('D', 'C'))
    print("Shortest path from E to D:", g.shortest_path('E', 'D'))
    print("Shortest path from C to E:", g.shortest_path('C', 'E'))
    print("Shortest path from B to D:", g.shortest_path('B', 'D'))
    print("Shortest path from D to B:", g.shortest_path('D', 'B'))
    print("Shortest path from E to C:", g.shortest_path('E', 'C'))
