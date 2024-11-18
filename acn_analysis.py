import argparse
import networkx as nx
import csv


def read_graph(file):
    # Read graph from .dot file and turn it into a networkx graph
    # https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pydot.read_dot.html
    dot_graph = nx.Graph(nx.drawing.nx_pydot.read_dot(file))

    return dot_graph


# Delete nodes with one neighbor until list_neighbor_1 is empty
def delete_neighbor_1(nx_graph):
    list_neighbor_1 = []

    for n in nx_graph.degree():
        if n[1] == 1:
            list_neighbor_1.append(n[0])

    while len(list_neighbor_1) > 0:
        for m in list_neighbor_1:
            nx_graph.remove_node(m)

        list_neighbor_1 = []

        for l in nx_graph.degree():
            if l[1] == 1:
                list_neighbor_1.append(l[0])

    return nx_graph


# Delete nodes with no neighbor
def delete_neighbor_0(nx_graph):
    list_neighbor_0 = []

    for n in nx_graph.degree():
        if n[1] == 0:
            list_neighbor_0.append(n[0])

    for m in list_neighbor_0:
        nx_graph.remove_node(m)

    return nx_graph


# Save adapted .dot graph
def write_graph(file, filename):
    nx.Graph(nx.drawing.nx_pydot.write_dot(file, filename))


# Determine number of nodes of .dot graph
def determine_nodes(nx_graph):
    nodes = list(nx_graph.nodes)

    print('nodes: ' + str(len(nodes)))

    return nodes


# Determine number of edges of .dot graph
def determine_edges(nx_graph):
    edges = list(nx_graph.edges)

    print('edges: ' + str(len(edges)))

    return edges


# Determine Euler number based on number of nodes and edges
def calculate_euler_number(nx_graph):
    # euler_number = nodes - edges
    nodes = list(nx_graph.nodes)
    edges = list(nx_graph.edges)

    euler_number = len(nodes) - len(edges)

    print('Euler number: ' + str(euler_number))
    return euler_number


# Determine cycle basis of .dot graph (number of SCL)
def determine_cycle_basis(nx_graph):
    basis = nx.cycle_basis(nx_graph)

    print('polygons/SCL: ' + str(len(basis)))

    return basis


def write_csv(numbnodes, numbedges, euler, numbpolygons, output):
    with open(output, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
        csvwriter.writerow(['number of nodes', 'number of edges', 'Euler number', 'number of polygons'])
        csvwriter.writerow([numbnodes, numbedges, euler, numbpolygons])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Deletes all nodes with one neighbor in a .dot graph, '
                                                 'returns number of nodes, edges, Euler number and number of polygons.')
    parser.add_argument('input_file', action='store', type=str, help='.dot file to analyze')
    parser.add_argument('-o', '--output_file', action='store', type=str, required=False, default='delete_n1.dot',
                        help='Name of output dot file.')
    parser.add_argument('-d', '--data_file', action='store', type=str, required=False, default='data.csv',
                        help='Name of output csv file which contains numer of nodes, edges, Euler number and '
                             'number of polygons.')

    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file
    data_file = args.data_file

    graph = read_graph(input_file)

    graph_delete = delete_neighbor_1(graph)

    delete_neighbor_0(graph_delete)

    write_graph(graph_delete, output_file)

    nodes = len(determine_nodes(graph_delete))

    edges = len(determine_edges(graph_delete))

    euler = calculate_euler_number(graph_delete)

    polygons = len(determine_cycle_basis(graph_delete))

    write_csv(nodes, edges, euler, polygons, data_file)
