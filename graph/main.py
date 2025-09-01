class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, " : ", self.adj_list.keys())


myGraoh = Graph()
myGraoh.add_vertex("A")

print(myGraoh.print_graph())


# {
#     "A": ["C", "B"],
#     "B": [],
#     "C": [],
#     "D": [],
#     "E": [],
# }
