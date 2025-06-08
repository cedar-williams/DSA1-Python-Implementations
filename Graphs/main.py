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

test_dfs()