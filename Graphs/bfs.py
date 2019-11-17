"""

Implementation of the Breadth-First Search (BFS)
This algorithm traverses a tree exploring all of the current node's options before moving onto the next.
"""


class Edge:
    def __init__(self, a, b):
        self.src = a
        self.dest = b

    def __str__(self):
        return "(" + str(self.src) + ", " + str(self.dest) + ")"


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, edge):
        """
        Adds new edge to the graph
        :param edge:
        :return:
        """
        self.graph.append(edge)

    def print_graph(self):
        print("This graph contains the following edges: ")
        for edge in self.graph:
            print("Edge: " + str(edge))


if __name__ == '__main__':
    graph = Graph(5)
    edge1 = Edge(1, 5)
    edge2 = Edge(1, 6)
    edge3 = Edge(1, 7)

    graph.add_edge(edge1)
    graph.add_edge(edge2)
    graph.add_edge(edge3)

    graph.print_graph()
