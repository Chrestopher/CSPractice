"""

Implementation of the Prim's Algorithm
This algorithm finds the Minimum Cost Spanning Tree (MCST) of a graph.
"""


class Edge:
    def __init__(self, a, b, c):
        self.src = a
        self.dest = b
        self.weight = c

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
    edge1 = Edge(1, 5, 1)
    edge2 = Edge(1, 6, 2)
    edge3 = Edge(1, 7, 3)
    edge4 = Edge(5, 6, 8)

    graph.add_edge(edge1)
    graph.add_edge(edge2)
    graph.add_edge(edge3)
    graph.add_edge(edge4)

    graph.print_graph()
