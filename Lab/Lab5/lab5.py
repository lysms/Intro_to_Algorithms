def explore(G, v):
    visited[v] = True
    for i in range(0, len(G[v])):
        if visited[G[v][i] - 1] == False:
            explore(G, G[v][i] - 1)

    # Store the node value
    node.append(v)


def dfs(G):
    clock = 1
    for v in range(0, len(G)):
        visited[v] = False
    for v in range(0, len(G)):
        if visited[v] == False:
            explore(G, v)


def construct_graph(G):
    for i in range(0, len(G)):
        for j in range(0, len(G[i])):
            Graph[G[i][j] - 1].append(i + 1)


filename = input("Enter the file that you want to read ==> ")
file = open(filename, "r")
input = []
for line in file:
    temp = line.rstrip("\n").split(" ")
    input.append(temp)

adj_list = []
Graph = []
connected = []
node = []

for i in range(0, len(input)):
    while len(adj_list) < int(input[i][0]):
        adj_list.append([])
        Graph.append([])
    adj_list[int(input[i][0]) - 1].append(int(input[i][1]))

# print(G)
# print("The Adjcency List is:", adj_list)
visited = len(adj_list) * [False]
pre = len(adj_list) * [0]
post = len(adj_list) * [0]

construct_graph(adj_list)

dfs(Graph)

# print(node)
node.reverse()
new_node = node[:]

visited = len(adj_list) * [False]
checked = len(adj_list) * [False]
total = 0

# Strongly Connected Component
for i in range(0, len(adj_list)):
    if total >= len(new_node):
        break
    sink = new_node[total]
    explore(adj_list, sink)
    temp = []
    for j in range(0, len(visited)):
        if visited[j] == True and checked[j] == False:
            temp.append(j + 1)
            checked[j] = True
            total += 1
    connected.append(temp)


for i in connected:
    print(i)
