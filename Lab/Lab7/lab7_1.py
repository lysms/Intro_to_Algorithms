import heapdict

H = heapdict.heapdict()
INF = 99999
V = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
E = [
    ("A-B", 10),
    ("A-C", 12),
    ("B-C", 9),
    ("B-D", 8),
    ("C-E", 3),
    ("C-F", 1),
    ("D-E", 7),
    ("D-G", 8),
    ("D-H", 5),
    ("E-F", 3),
    ("F-H", 6),
    ("G-H", 9),
    ("G-I", 2),
    ("H-I", 11),
]
U = ["A", "D", "F"]
weight = {}
Graph = {}

for i in E:
    edge = i[0].split("-")
    edge = tuple(edge)
    w = i[1]
    weight[edge] = w
    H[edge] = w
    u = edge[0]
    v = edge[1]
    if u in Graph:
        Graph[u].append(v)
    else:
        Graph[u] = list()
        Graph[u].append(v)

    if v not in Graph:
        Graph[v] = list()
        Graph[v].append(u)
    else:
        Graph[v].append(u)
print(weight)
print(Graph)

visited = len(V) * [False]


num_edge = 0
total = 0

