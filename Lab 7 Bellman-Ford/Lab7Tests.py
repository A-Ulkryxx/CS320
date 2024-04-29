from edgegraph import *
from main import bellman_ford


graph = GraphEL()

v1 = VertexEL("A")
v2 = VertexEL("B")
v3 = VertexEL("C")
v4 = VertexEL("D")
v5 = VertexEL("E")
v6 = VertexEL("F")
v7 = VertexEL("Z")
# check for graph None
assert(bellman_ford(graph, v1, v2 ) == [])

graph.add_vertex(v1)
graph.add_vertex(v2)
graph.add_vertex(v3)
graph.add_vertex(v4)
graph.add_vertex(v5)
graph.add_vertex(v6)

# check for vertices of none
assert(bellman_ford(graph, None, v2 ) == [])
assert(bellman_ford(graph, v1, None ) == [])

# check for vertice not in graph
assert(bellman_ford(graph, v7, v2 ) == [])
assert(bellman_ford(graph, v1, v7 ) == [])

edge1 = EdgeEL("A2B", v1, v2)
edge1.set_value(5)
edge2 = EdgeEL("B2C", v2, v3)
edge2.set_value(1)
edge3 = EdgeEL("B2D", v2, v4)
edge3.set_value(2)
edge4 = EdgeEL("C2E", v3, v5)
edge4.set_value(1)
edge5 = EdgeEL("E2D", v5, v4)
edge5.set_value(-1)
edge6 = EdgeEL("D2F", v4, v6)
edge6.set_value(2)
edge7 = EdgeEL("F2E", v6, v5)
edge7.set_value(3)

graph.add_edge(edge1)
graph.add_edge(edge2)
graph.add_edge(edge3)
graph.add_edge(edge4)
graph.add_edge(edge5)
graph.add_edge(edge6)
graph.add_edge(edge7)

# check for negative weights
assert(bellman_ford(graph, v1, v6) == [])

graph.rm_edge(edge5)
edge5.set_value(1)
graph.add_edge(edge5)

assert(bellman_ford(graph, v1, v6) == [v1, v2, v4, v6])