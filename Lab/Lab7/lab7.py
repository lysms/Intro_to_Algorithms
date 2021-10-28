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
U = ["A", "F", "G", "C", "H"]
U = ["A", "F", "G"]


def prim(Graph):
    num_nodes = len(Graph)
    visited = len(Graph) * [False]
    g = []
    for i in U:
        g.append(V.index(i))
    num_edges = 0
    visited[0] = True
    max_v = max(g)
    marked = len(g) * [False]

    total = 0
    while num_edges < num_nodes - 1:
        success = False
        minimum = 9999
        a = 0
        b = 0
        for m in range(max_v + 1):
            if visited[m]:
                if V[m] in U:
                    if not marked[U.index(V[m])]:
                        for n in range(max_v + 1):
                            if (not visited[n]) and Graph[m][n]:

                                # not in selected and there is an edge
                                if minimum > Graph[m][n] + 1:
                                    minimum = Graph[m][n]
                                    a = m
                                    b = n
                                    success = True
                else:
                    for n in range(max_v + 1):
                        if (not visited[n]) and Graph[m][n]:

                            # not in selected and there is an edge
                            if minimum > Graph[m][n] + 1:
                                minimum = Graph[m][n]
                                a = m
                                b = n
                                success = True
        if success:
            print("{}---{} : {:2d}".format(V[a], V[b], Graph[a][b]))
            if V[a] in U:
                marked[U.index(V[a])] = True
                # print(U.index(V[a]))

            elif V[b] in U:
                marked[U.index(V[b])] = True
                # print(U.index(V[b]))
            total += int(Graph[a][b])
        visited[b] = True
        num_edges += 1
    print("The toal weights is:", total, "\n")


if __name__ == "__main__":
    weight = {}
    Graph = {}
    for i in E:
        edge = i[0].split("-")
        edge = tuple(edge)
        w = i[1]
        weight[edge] = w
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

    Graph = [
        [0, 10, 12, 0, 0, 0, 0, 0, 0],
        [10, 0, 9, 8, 0, 0, 0, 0, 0],
        [12, 9, 0, 0, 3, 1, 0, 0, 0],
        [0, 8, 0, 0, 7, 0, 8, 5, 0],
        [0, 0, 3, 7, 0, 3, 0, 0, 0],
        [0, 0, 1, 0, 3, 0, 0, 6, 0],
        [0, 0, 0, 8, 0, 0, 0, 9, 2],
        [0, 0, 0, 5, 0, 6, 9, 0, 11],
        [0, 0, 0, 0, 0, 0, 2, 11, 0],
    ]
    print("\nThe spanning tree is: ")
    prim(Graph)
