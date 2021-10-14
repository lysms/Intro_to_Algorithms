# 1 2 ===> 1 has a line to 2


if __name__ == "__main__":
    file = open("lab5_1.txt", "r")
    input = list()
    for line in file:
        temp = line.strip("\n").split()
        input.append(temp)

    print(input[0][0])
    print(len(input))
    adj_list = {}

    for i in range(0, len(input)):
        print(i)
        if int(input[i][0]) not in adj_list:
            adj_list[int(input[i][0])] = list()
        adj_list[int(input[i][0])].append(int(input[i][1]))
    print(adj_list)
