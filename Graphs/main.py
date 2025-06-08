from Graph import Vertex, Graph
from Queues.Queue import Queue, Node

def breadth_first_search(graph, start_vertex, distances=dict()):
    discovered_set = set()
    frontier_queue = Queue()
    visited_list = []

    # Starting point is 0 from itself
    distances[start_vertex] = 0

    frontier_queue.enqueue(start_vertex)
    discovered_set.add(start_vertex)

    while frontier_queue.peek() is not None:
        current_vertex = frontier_queue.dequeue()
        visited_list.append(current_vertex)
        for adjacent_vertex in graph.adjacency_list[current_vertex]:
            if adjacent_vertex not in discovered_set:
                frontier_queue.enqueue(adjacent_vertex)
                discovered_set.add(adjacent_vertex)

                distances[adjacent_vertex] = distances[current_vertex] + 1

    return visited_list


g = Graph()
vertex_a = Vertex('Joe')
vertex_b = Vertex('Eva')
vertex_c = Vertex('Taj')
vertex_d = Vertex('Chen')
vertex_e = Vertex('Lily')
vertex_f = Vertex('Jun')
vertex_g = Vertex('Ken')
vertices = [vertex_a, vertex_b, vertex_c, vertex_d, vertex_e, vertex_f, vertex_g]

# Add each vertex to the graph
for vertex in vertices:
    g.add_vertex(vertex)

# Add graph edges
g.add_undirected_edge(vertex_a, vertex_b)  # Edge from Joe to Eva
g.add_undirected_edge(vertex_a, vertex_c)  # Edge from Joe to Taj
g.add_undirected_edge(vertex_b, vertex_e)  # Edge from Eva to Lily
g.add_undirected_edge(vertex_c, vertex_d)  # Edge from Taj to Chen
g.add_undirected_edge(vertex_c, vertex_e)  # Edge from Taj to Lily
g.add_undirected_edge(vertex_d, vertex_f)  # Edge from Chen to Jun
g.add_undirected_edge(vertex_e, vertex_f)  # Edge from Lily to Jun
g.add_undirected_edge(vertex_f, vertex_g)  # Edge from Jun to Ken

start_name = input('Enter the starting person\'s name: ')
print()

# Search for the start vertex
start_vertex = None
for vertex in vertices:
    if vertex.label == start_name:
        start_vertex = vertex

if start_vertex is None:
    print('Start vertex "%s" not found' % start_name)
else:
    vertex_distances = dict()
    visited_list = breadth_first_search(g, start_vertex, vertex_distances)

    # Output
    print('Breadth-first search traversal')
    print('Start vertex: %s' % start_vertex.label)
    for vertex in visited_list:
        print('%s: %d' % (vertex.label, vertex_distances[vertex]))