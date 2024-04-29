from edgegraph import GraphEL, VertexEL


def check_cases(graph, start):
    if graph is None:
        return True
    elif start is None:
        return True
    vertices = graph.vertices()
    if (start not in vertices):
        return True
    return False


def bfs(graph, start):
    if check_cases(graph, start):
        return []

    ordered = []
    queue = []
    visited = []
    visited.append(start)
    queue.append(start)

    while queue != []:
        current = queue.pop(0)
        ordered.append(current)
        for edge in graph.incident(current):
            neighbors = edge.ends()
            if neighbors[0] != current:
                neighbor = neighbors[0]  
            else:
                neighbor = neighbors[1]
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return ordered
