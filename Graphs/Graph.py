class Vertex:
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None

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

    def get_vertex(self, vertex_label):
        for vertex in self.adjacency_list:
            if vertex.label == vertex_label:
                return vertex
        return None

    def get_vertex_list(self):
        return list(self.adjacency_list)

    def get_incoming_edges(self, vertex):
        incoming_edges = []
        for edge in self.edge_weights:
            if edge[1] is vertex:
                incoming_edges.append(edge)
        return incoming_edges