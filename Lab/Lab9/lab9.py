def matrixChain(matrix):
    length = len(matrix) - 1

    c = []
    for i in range(length):
        temp = []
        for j in range(length):
            temp.append(0)
        c.append(temp)

    n = length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            c[i][j] = 100000
            k = i
            while k < j:
                # c(i, j) = min{C(i, k) + c(k + 1, j) + m[i - 1] * m[k] * m[j] : i <= k < j}
                cost = c[i][k] + c[k + 1][j] + matrix[i] * matrix[k + 1] * matrix[j + 1]
                if cost < c[i][j]:
                    c[i][j] = cost
                    c[j][i] = k + 1
                k += 1

    # print(c)
    print("The cost is ==> {}".format(c[0][n - 1]))
    return c


def parenthesization(c, j, i):
    if j == i:
        # Print the letter in order A. B. C
        print(chr(65 + j), end="")
        return
    else:
        print("(", end="")
        # Do the parenthes in oppposite order. Since we did the subproblem reversively. And the order of the value that add-up on the char is in the last list of the list.
        parenthesization(c, c[j][i] - 1, i)
        parenthesization(c, j, c[j][i])
        print(")", end="")


if __name__ == "__main__":

    matrix = [50, 20, 1, 10, 100]
    matrix = [10, 20, 30, 40, 50, 40, 10, 50, 20]

    c = matrixChain(matrix)
    # for i in c:
    #     print(i)
    print("The Parenthesization is ==> ", end="")
    parenthesization(c, len(matrix) - 2, 0)
