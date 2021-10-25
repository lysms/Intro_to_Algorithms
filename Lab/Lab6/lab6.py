import heapdict


def dijkstra(G, l, s):
    dist = len(G) * [float("inf")]
    dist[s] = 0
    prev = dict()
    H = heapdict.heapdict()
    for i in range(0, len(G)):
        H[i] = dist[i]
        prev[i] = None

    # print(H)
    while len(H.keys()) != 0:

        u = H.popitem()
        # print("This is value of u", u)
        # print(G[u[0]])
        for i in range(len(G[u[0]])):
            # print(G[u[0][i]])
            # Go over the graph to check the length, and assign it into the heapdict.
            if dist[G[u[0]][i]] > dist[u[0]] + l[u[0]][i]:
                dist[G[u[0]][i]] = dist[u[0]] + l[u[0]][i]
                prev[G[u[0]][i]] = u[0]
                H[G[u[0]][i]] = dist[G[u[0]][i]]

    shortest_paths = []
    for i in range(1, len(prev)):
        tmp = prev[i]
        # print(tmp)
        l = dist[i]
        small_path = [l, [i]]
        # print(small_path)
        while tmp != None:
            # print(tmp)
            if tmp != None:
                small_path[1].append(tmp)
            tmp = prev[tmp]
        small_path[1].reverse()
        print(small_path)
        shortest_paths.append(small_path)
    return shortest_paths


if __name__ == "__main__":
    file_r = open("example.txt", "r")
    # file_r = open("rome99.txt", "r")
    file_w = open("lab6_output.txt", "w")

    line = [i.strip("\n").split() for i in file_r]
    file_r.close()

    Graph = list()
    Weight = list()

    # Construct the graph and prepare for the bfs
    for i in range(0, len(line)):
        while len(Graph) < int(line[i][0]) + 1:
            Graph.append([])
            Weight.append([])
        Weight[int(line[i][0])].append(int(line[i][2]))
        Graph[int(line[i][0])].append(int(line[i][1]))
    shortest_path = dijkstra(Graph, Weight, 1)
    # print(shortest_path)
    for i in range(0, len(shortest_path)):
        file_w.write(
            (
                "{:4d}: {:5d}, {}\n".format(
                    i + 1, shortest_path[i][0], shortest_path[i][1]
                )
            )
        )

    file_w.close()
