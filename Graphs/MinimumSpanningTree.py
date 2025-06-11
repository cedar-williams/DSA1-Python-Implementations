import heapq
from Graph import Graph, VertexG

class EdgeWeight:
    def __init__(self, from_vertex, to_vertex, weight):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __ne__(self, other):
        return self.weight != other.weight

class VertexSetCollection:
    def __init__(self, all_vertices):
        self.vertex_map = dict()
        for vertex in all_vertices:
            vertex_set = set()
            vertex_set.add(vertex)
            self.vertex_map[vertex] = vertex_set

    def __len__(self):
        return len(self.vertex_map)

    def get_set(self, vertex):
        return self.vertex_map[vertex]

    # Combine both sets, point all vertex's in each set at merged set
    def merge(self, vertex_set1, vertex_set2):
        merged = vertex_set1.union(vertex_set2)
        for vertex in merged:
            self.vertex_map[vertex] = merged

def minimum_spanning_tree(graph):
    # Create a list of all edges in the graph
    edge_list = []
    for edge in graph.edge_weights:
        edge_weight = EdgeWeight(edge[0], edge[1], graph.edge_weights[edge])
        edge_list.append(edge_weight)

    # Turn it into a priority queue
    heapq.heapify(edge_list)

    vertex_set = VertexSetCollection(graph.adjacency_list)

    results_list = []

    while len(vertex_set) > 1 and len(edge_list) > 0:
        next_edge = heapq.heappop(edge_list)
        set1 = vertex_set.get_set(next_edge.from_vertex)
        set2 = vertex_set.get_set(next_edge.to_vertex)
        if set1 is not set2:
            results_list.append(next_edge)
            vertex_set.merge(set1, set2)

    return results_list

graph1 = Graph()

# Add vertices A through H
vertex_names = ["A", "B", "C", "D", "E", "F", "G", "H"]
for vertex_name in vertex_names:
    graph1.add_vertex(Vertex(vertex_name))

# Add edges
graph1.add_undirected_edge(graph1.get_vertex("A"), graph1.get_vertex("B"), 15)
graph1.add_undirected_edge(graph1.get_vertex("A"), graph1.get_vertex("D"), 6)
graph1.add_undirected_edge(graph1.get_vertex("B"), graph1.get_vertex("C"), 9)
graph1.add_undirected_edge(graph1.get_vertex("B"), graph1.get_vertex("D"), 12)
graph1.add_undirected_edge(graph1.get_vertex("B"), graph1.get_vertex("G"), 14)
graph1.add_undirected_edge(graph1.get_vertex("B"), graph1.get_vertex("H"), 10)
graph1.add_undirected_edge(graph1.get_vertex("C"), graph1.get_vertex("E"), 16)
graph1.add_undirected_edge(graph1.get_vertex("D"), graph1.get_vertex("E"), 8)
graph1.add_undirected_edge(graph1.get_vertex("E"), graph1.get_vertex("F"), 20)

# Get the list of edges for the graph's minimum spanning tree
tree_edges = minimum_spanning_tree(graph1)

# Display the list of edges
print("Edges in minimum spanning tree (graph 1):")
for edge in tree_edges:
    print(edge.from_vertex.label + " to " + edge.to_vertex.label, end="")
    print(", weight = " + str(edge.weight))

# Main program 2
graph2 = Graph()

# Add vertices A through G, and P
vertex_names = ["A", "B", "C", "D", "E", "F", "G", "P"]
for vertex_name in vertex_names:
    graph2.add_vertex(Vertex(vertex_name))

# Add edges
graph2.add_undirected_edge(graph2.get_vertex("A"), graph2.get_vertex("B"), 80)
graph2.add_undirected_edge(graph2.get_vertex("A"), graph2.get_vertex("C"), 105)
graph2.add_undirected_edge(graph2.get_vertex("A"), graph2.get_vertex("E"), 182)
graph2.add_undirected_edge(graph2.get_vertex("B"), graph2.get_vertex("C"), 90)
graph2.add_undirected_edge(graph2.get_vertex("B"), graph2.get_vertex("D"), 60)
graph2.add_undirected_edge(graph2.get_vertex("B"), graph2.get_vertex("P"), 100)
graph2.add_undirected_edge(graph2.get_vertex("C"), graph2.get_vertex("P"), 132)
graph2.add_undirected_edge(graph2.get_vertex("D"), graph2.get_vertex("E"), 80)
graph2.add_undirected_edge(graph2.get_vertex("E"), graph2.get_vertex("F"), 70)
graph2.add_undirected_edge(graph2.get_vertex("F"), graph2.get_vertex("G"), 72)
graph2.add_undirected_edge(graph2.get_vertex("F"), graph2.get_vertex("P"), 145)
graph2.add_undirected_edge(graph2.get_vertex("G"), graph2.get_vertex("P"), 180)

# Get the list of edges for the graph's minimum spanning tree
tree_edges = minimum_spanning_tree(graph2)

# Display the list of edges
print("Edges in minimum spanning tree (graph 2):")
for edge in tree_edges:
    print(edge.from_vertex.label + " to " + edge.to_vertex.label, end="")
    print(", weight = " + str(edge.weight))
