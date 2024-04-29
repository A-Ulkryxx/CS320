from edgegraph import *


def check_cases(graph, start, end):
    if graph is None or start is None or end is None:
        return True
    if start not in graph.vertices() or end not in graph.vertices():
        return True
    return False


def get_graph_details(graph):
    num_verts = graph.num_vertices()
    distances = [float("Inf")] * num_verts
    vertices = graph.vertices()
    previous_verts = [None] * num_verts
    return num_verts, distances, vertices, previous_verts


def get_edge_details(edge, vertices):
    u, z = edge.ends()
    u_ind = vertices.index(u)
    z_ind = vertices.index(z)
    edge_val = edge.get_value()
    return u_ind, z_ind, edge_val


def get_shortest_path(end, vertices, previous_verts):
    shortest_path = []
    index = vertices.index(end)
    while index is not None:
        shortest_path.append(vertices[index])
        index = previous_verts[index]
    shortest_path.reverse()
    return shortest_path


def bellman_ford(graph: GraphEL, start: VertexEL, end: VertexEL) -> list:
    if check_cases(graph, start, end):
        return []
    num_verts, distances, vertices, previous_verts = get_graph_details(graph)
    v_ind = vertices.index(start)
    distances[v_ind] = 0

    for i in range(0, num_verts - 1):
        for edge in graph.edges():
            u_ind, z_ind, edge_val = get_edge_details(edge, vertices)
            if edge_val <= 0:
                return []
            if ((distances[u_ind] + edge_val) < distances[z_ind]):
                distances[z_ind] = distances[u_ind] + edge_val
                previous_verts[z_ind] = u_ind

    return get_shortest_path(end, vertices, previous_verts)
