from typing import Dict, List, Union

Vertex = Union[str, int]  # can store either strings or ints


class Graph:
    def __init__(self) -> None:
        self.adj_list: Dict[Vertex, List[Vertex]] = {}

    def add_vertex(self, vertex: Vertex) -> bool:
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def print_graph(self) -> None:
        for vertex, edges in self.adj_list.items():
            print(vertex, " : ", edges)

    def add_edges(self, v1: Vertex, v2: Vertex) -> bool:
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1: Vertex, v2: Vertex) -> bool:
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

    def remove_vertex(self, v1: Vertex) -> bool:
        if v1 in self.adj_list.keys():
            for other_vertex in self.adj_list[v1]:
                self.adj_list[other_vertex].remove(v1)
            del self.adj_list[v1]
            return True
        return False


# Example usage
#      A
#     /  \
#   B------C
#
#

my_graph = Graph()

my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")

my_graph.add_edges("A", "B")
my_graph.add_edges("B", "C")
my_graph.add_edges("C", "A")

my_graph.print_graph()
