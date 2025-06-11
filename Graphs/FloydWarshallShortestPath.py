from Graph import Vertex, Graph

def all_pairs_shortest_path(graph):
    vertices = graph.get_vertex_list()
    num_vertices = len(vertices)

    # Create the matrix with all values to infinity
    dist_matrix = []
    for i in range(0, num_vertices):
        dist_matrix.append([float('inf')] * num_vertices)

    # When an entry points to itself the distance is 0
    for i in range(0, num_vertices):
        dist_matrix[i][i] = 0

    # When an entry is already a defined edge w/ a weight we insert that right away
    for edge in graph.edge_weights:
        dist_matrix[vertices.index(edge[0])][vertices.index(edge[1])] = graph.edge_weights[edge]

    for k in range(0, num_vertices):
        for to_index in range(0, num_vertices):
            for from_index in range(0, num_vertices):
                current_length = dist_matrix[from_index][to_index]
                possible_length = dist_matrix[from_index][k] + dist_matrix[k][to_index]
                if possible_length < current_length:
                    dist_matrix[from_index][to_index] = possible_length

    return dist_matrix

def reconstruct_path(graph, start_vertex, end_vertex, dist_matrix=None):
    if dist_matrix is None:
        dist_matrix = all_pairs_shortest_path(graph)

    vertices = graph.get_vertex_list()
    start_index = vertices.index(start_vertex)
    path = []

    # Work back from last vertex to start
    current_index = vertices.index(end_vertex)
    while current_index != start_index:
        incoming_edges = graph.get_incoming_edges(vertices[current_index])
        found_next = False
        for current_edge in incoming_edges:
            expected = dist_matrix[start_index][current_index] - graph.edge_weights[current_edge]
            actual = dist_matrix[start_index][vertices.index(current_edge[0])]
            if expected == actual:
                current_index = vertices.index(current_edge[0])
                path = [current_edge] + path
                found_next = True
                break

        if found_next is False:
            return None
    return path

# START NOT MY CODE

def display_matrix(matrix, vertices):
    # This function assumes a simple square matrix, where each entry is either
    # an integer in the range [-99, 99], or infinity. Each vertex's label is
    # also assumed to be a single character.

    # First print column headers
    print("   ", end="")
    for entryIndex in range(len(matrix)):
        print("  %s" % vertices[entryIndex].label, end=" ")
    print()

    for row_index in range(len(matrix)):
        row = matrix[row_index]
        print("%s [ " % vertices[row_index].label, end="")
        for entry in row:
            # Case 1: entry is infinity
            if entry == float("inf"):
                print("inf", end=" ")

            # Case 2: entry is negative
            elif entry < 0:
                # Case 2A: entry is > -10
                if entry > -10:
                    print(str(entry), end="  ")
                # Case 2B: entry is <= -10
                else:
                    print(str(entry), end=" ")


            # Case 3: entry is non-negative
            else:
                # Case 3A: entry is < 10
                if entry < 10:
                    print(" " + str(entry) + " ", end=" ")
                # Case 3B: entry is >= 10
                else:
                    print(" " + str(entry), end=" ")
        print("]")


# Main program

graphs = [
    # Graph 1
    (["A", "B", "C", "D"],
     [("A", "B", 2), ("B", "C", -3), ("B", "D", 7), ("C", "A", 5), ("D", "A", -4)],
     "C", "D"  # show path from C to D
     ),

    # Graph 2
    (["A", "B", "C", "D"],
     [("A", "B", 4), ("B", "C", 3), ("C", "D", 6), ("D", "A", -1), ("D", "B", 7)],
     "D", "B"  # show path from D to B
     ),

    # Graph 3
    (["A", "B", "C"],
     [("A", "B", 1), ("A", "C", 1), ("B", "C", -8)],
     "C", "A"  # show path from C to A (no path)
     ),

    # Graph 4
    (["A", "B", "C", "D", "E"],
     [("A", "B", 1), ("A", "E", 8), ("B", "C", 2), ("C", "D", 3), ("D", "A", -5), ("E", "D", 9)],
     "A", "D"  # show path from A to D
     )
]

# Run samples for each graph defined above
graph_number = 1
for graph_desc in graphs:
    graph = Graph()

    # Add vertices
    vertex_names = graph_desc[0]
    for vertex_name in vertex_names:
        graph.add_vertex(Vertex(vertex_name))
    # Add edges
    edge_tuples = graph_desc[1]
    for edge_tuple in edge_tuples:
        graph.add_directed_edge(graph.get_vertex(edge_tuple[0]), graph.get_vertex(edge_tuple[1]), edge_tuple[2])

    # Get the matrix for all pairs shortest path
    matrix = all_pairs_shortest_path(graph)

    # Display the matrix
    print("All-pairs shortest path matrix (graph %d):" % graph_number)
    display_matrix(matrix, graph.get_vertex_list())

    # Show an actual path sequence
    print("Shortest path from %s to %s:" % (graph_desc[2], graph_desc[3]))
    start_vertex = graph.get_vertex(graph_desc[2])
    end_vertex = graph.get_vertex(graph_desc[3])
    path = reconstruct_path(graph, start_vertex, end_vertex, matrix)
    if path is None or len(path) == 0:
        print("No path")
    else:
        print(path[0][0].label, end="")
        for edge in path:
            print(" to " + str(edge[1].label), end="")
        print()
    print()

    # Increment graph number for next example
    graph_number = graph_number + 1
