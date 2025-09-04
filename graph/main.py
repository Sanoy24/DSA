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


# Example usage
myGraph = Graph()
myGraph.add_vertex("A")
myGraph.add_vertex("B")
myGraph.add_edges("A", "B")

myGraph.print_graph()
