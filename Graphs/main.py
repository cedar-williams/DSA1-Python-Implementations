from Graph import Vertex, Graph
from Queues.Queue import Queue, Node
import operator

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

def test_bfs():
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

def depth_first_search(graph, start_vertex, visit_function):
    vertex_stack = [start_vertex]
    visited_set = set()

    while len(vertex_stack) > 0:
        current_vertex = vertex_stack.pop()
        if current_vertex not in visited_set:
            visit_function(current_vertex)
            visited_set.add(current_vertex)
            for adjacent_vertex in graph.adjacency_list[current_vertex]:
                vertex_stack.append(adjacent_vertex)

def test_dfs():
    # Main program - Creates 3 different graphs, each with vertices A through F, but with
    # different sets of edges. Traverses each with DFS.
    vertex_names = ["A", "B", "C", "D", "E", "F"]

    # Add the same set of vertices to 3 different graphs
    graph1 = Graph()
    graph2 = Graph()
    graph3 = Graph()
    graphs = [graph1, graph2, graph3]
    for vertex_name in vertex_names:
        for graph in graphs:
            graph.add_vertex(Vertex(vertex_name))

    # Add graph 1's edges
    graph1.add_undirected_edge(graph1.get_vertex("A"), graph1.get_vertex("B"))
    graph1.add_undirected_edge(graph1.get_vertex("A"), graph1.get_vertex("D"))
    graph1.add_undirected_edge(graph1.get_vertex("B"), graph1.get_vertex("E"))
    graph1.add_undirected_edge(graph1.get_vertex("B"), graph1.get_vertex("F"))
    graph1.add_undirected_edge(graph1.get_vertex("C"), graph1.get_vertex("F"))
    graph1.add_undirected_edge(graph1.get_vertex("E"), graph1.get_vertex("F"))

    # Add graph 2's edges
    graph2.add_undirected_edge(graph2.get_vertex("A"), graph2.get_vertex("B"))
    graph2.add_undirected_edge(graph2.get_vertex("B"), graph2.get_vertex("C"))
    graph2.add_undirected_edge(graph2.get_vertex("C"), graph2.get_vertex("F"))
    graph2.add_undirected_edge(graph2.get_vertex("D"), graph2.get_vertex("E"))
    graph2.add_undirected_edge(graph2.get_vertex("E"), graph2.get_vertex("F"))

    # Add graph 3's edges
    graph3.add_undirected_edge(graph3.get_vertex("A"), graph3.get_vertex("B"))
    graph3.add_undirected_edge(graph3.get_vertex("A"), graph3.get_vertex("E"))
    graph3.add_undirected_edge(graph3.get_vertex("B"), graph3.get_vertex("C"))
    graph3.add_undirected_edge(graph3.get_vertex("B"), graph3.get_vertex("E"))
    graph3.add_undirected_edge(graph3.get_vertex("C"), graph3.get_vertex("E"))
    graph3.add_undirected_edge(graph3.get_vertex("D"), graph3.get_vertex("E"))
    graph3.add_undirected_edge(graph3.get_vertex("E"), graph3.get_vertex("F"))

    # Create a visitor function that displays a vertex's label
    visitor = lambda x: print(x.label, end=' ')

    # Choose a starting vertex
    start_vertex_label = "A"

    # Visit vertices in each graph with DFS
    print('Depth-first search traversal')
    for i in range(0, len(graphs)):
        print('Graph ' + str(i + 1) + ': ', end='')
        depth_first_search(graphs[i], graphs[i].get_vertex(start_vertex_label), visitor)
        print()

def dijkstras_shortest_path(graph, start_vertex):
    """Updates values on the vertexs"""
    # Schlep all the unvisisted vertexs into the unvisited queue
    unvisited_queue = []
    for current_vertex in graph.adjacency_list:
        unvisited_queue.append(current_vertex)

    start_vertex.distance = 0

    while len(unvisited_queue) > 0:

        # Visit closest vertex
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)

        # Check potential path lengths to all neighbours
        for adj_vertex in graph.adjacency_list[current_vertex]:
            edge_weight = graph.edge_weights[(current_vertex, adj_vertex)]
            alternative_path_distance = current_vertex.distance + edge_weight

            # If path is shorter set update the distance value and set as predecessor
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.prev_vertex = current_vertex

def get_shortest_path(start_vertex, end_vertex):
    path = ''
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = '->' + str(current_vertex.label) + path
        current_vertex = current_vertex.prev_vertex
    path = start_vertex.label + path
    return path

def test_dsp():
    # Program to find shortest paths from vertex A.
    g = Graph()

    vertex_a = Vertex("A")
    vertex_b = Vertex("B")
    vertex_c = Vertex("C")
    vertex_d = Vertex("D")
    vertex_e = Vertex("E")
    vertex_f = Vertex("F")
    vertex_g = Vertex("G")
    g.add_vertex(vertex_a)
    g.add_vertex(vertex_b)
    g.add_vertex(vertex_c)
    g.add_vertex(vertex_d)
    g.add_vertex(vertex_e)
    g.add_vertex(vertex_f)
    g.add_vertex(vertex_g)

    g.add_undirected_edge(vertex_a, vertex_b, 8)
    g.add_undirected_edge(vertex_a, vertex_c, 7)
    g.add_undirected_edge(vertex_a, vertex_d, 3)
    g.add_undirected_edge(vertex_b, vertex_e, 6)
    g.add_undirected_edge(vertex_c, vertex_d, 1)
    g.add_undirected_edge(vertex_c, vertex_e, 2)
    g.add_undirected_edge(vertex_d, vertex_f, 15)
    g.add_undirected_edge(vertex_d, vertex_g, 12)
    g.add_undirected_edge(vertex_e, vertex_f, 4)
    g.add_undirected_edge(vertex_f, vertex_g, 1)

    # Run Dijkstra's algorithm first.
    dijkstras_shortest_path(g, vertex_a)

    # Sort the vertices by the label for convenience; display shortest path for each vertex
    # from vertex_a.
    for v in sorted(g.adjacency_list, key=operator.attrgetter("label")):
        if v.pred_vertex is None and v is not vertex_a:
            print("A to %s: no path exists" % v.label)
        else:
            print("A to %s: %s (total weight: %g)" % (v.label, get_shortest_path(vertex_a, v), v.distance))

test_dsp()