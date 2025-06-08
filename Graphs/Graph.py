class Vertex:
    def __init__(self, label):
        self.label = label

class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex,to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, a_vertex, b_vertex, weight=1.0):
        self.add_directed_edge(a_vertex, b_vertex, weight)
        self.add_directed_edge(b_vertex, a_vertex, weight)


# Test code
g = Graph()
vertex_a = Vertex("1")
vertex_b = Vertex("2")
vertex_c = Vertex("3")
vertex_d = Vertex("4")
vertex_e = Vertex("5")
g.add_vertex(vertex_a)
g.add_vertex(vertex_b)
g.add_vertex(vertex_c)
g.add_vertex(vertex_d)
g.add_vertex(vertex_e)

g.add_directed_edge(vertex_a, vertex_b, 8)
g.add_directed_edge(vertex_a, vertex_c, 12)
g.add_directed_edge(vertex_a, vertex_d, 17)
g.add_directed_edge(vertex_b, vertex_e, 11)
g.add_directed_edge(vertex_e, vertex_c, 23)
g.add_directed_edge(vertex_c, vertex_d, 15)
g.add_directed_edge(vertex_e, vertex_d, 6)