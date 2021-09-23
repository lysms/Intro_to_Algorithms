import random
import timeit
import math

# sys.setrecursionlimit(150000)

# 13 * 11 ->> 13 is double, 11 is dropping which is x double, y dropping
def method1(x, y):
    result = 0

    # Keep going till the y number gets down to 1
    while y != 0:
        if y & 1:
            result += x
        x = x << 1  # shift left (double the second number each time)
        y = y >> 1  # shift right  (dropping each time by math.floor(y/2))



    return result


def method2(x, y):
    if y == 0:
        return 0
    z = method2(x, math.floor(y >> 1))
    if (y % 2) == 0:
        return z << 1
    else:
        return x + (z << 1)


def method3(x, y):
    n = max(x.bit_length(), y.bit_length())

    if n <= 1:
        return x & y

    half = n >> 1  # n/2

    xl = x >> half  # leftmost bits
    # for example x = 178, xl is leftmost, then tran is to the number less than the right-bit than original one, thus, use orig - tran
    tran = xl << half
    xr = x - tran

    yl = y >> half
    tran = yl << half
    yr = y - tran

    p1 = method3(xl, yl)
    p2 = method3(xr, yr)
    p3 = method3(xl + xr, yl + yr)
    return (
        p1 * (1 << ((math.floor(n >> 1)) << 1))  # p1 << ((math.floor(n >> 1)) << 1)
        + (p3 - p1 - p2)
        * (1 << (math.floor(n >> 1)))  # (p3-p1-p2) << (math.floor(n>>1))
        + p2
    )


if __name__ == "__main__":
    d = int(input("The number of digits: "))

    time1 = []
    time2 = []
    time3 = []
    for i in range(0, 10):
        x = random.randint(10 ** (d - 1), (10 ** d) - 1)
        y = random.randint(10 ** (d - 1), (10 ** d) - 1)
        # print(method2(x, y))
        # print(method3(x, y))

        time1.append(
            timeit.timeit(
                "method1(" + str(x) + "," + str(y) + ")",
                "from __main__ import method1",
                number=1,
            )
        )
        # time2.append(
        #     timeit.timeit(
        #         "method2(" + str(x) + "," + str(y) + ")",
        #         "from __main__ import method2",
        #         number=1,
        #     )
        # )
        time3.append(
            timeit.timeit(
                "method3(" + str(x) + "," + str(y) + ")",
                "from __main__ import method3",
                number=1,
            )
        )

    ave1 = float(sum(time1)) / 10
    ave2 = float(sum(time2)) / 10
    ave3 = float(sum(time3)) / 10
    print(
        "Average Times:\n",
        "\tMethod 1:",
        ave1,
        "\n\tMethod 2:",
        ave2,
        "\n\tMethod 3:",
        ave3,
    )

