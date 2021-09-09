import timeit
import matplotlib.pyplot as plt

# print("Enter a number to generate the n-th Fibonacci number")
# n = int(input())

n = [1, 5, 10, 15, 20, 25, 30, 35]
n_2 = [2 ** 10, 2 ** 12, 2 ** 14, 2 ** 16, 2 ** 18, 2 ** 19]


def fib1(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fib1(x - 1) + fib1(x - 2)


def fib2(x):
    fib = [0, 1]
    for n in range(2, x + 1):
        fib.append(fib[n - 2] + fib[n - 1])
    return fib[x]


def main():
    fib1_time_part1 = []
    fib2_time_part1 = []
    fib2_time_part2 = []

    ################################# part 1 fib1     ############################################
    print("Recursive algorithm")
    for number in n:
        value = fib1(number)
        timer = timeit.timeit(
            "fib1(" + str(number) + ")", "from __main__ import fib1", number=1
        )
        # timer1.autorange()
        fib1_time_part1.append(timer)
        print("fib1(", number, ") -> ", value, " = ", timer, " seconds", sep="")

    #############################################  PART 1  fib2  #################################################
    print("\nIterative algorithm")
    for number in n:
        value = fib2(number)
        timer = timeit.timeit(
            "fib2(" + str(number) + ")", "from __main__ import fib2", number=1
        )
        fib2_time_part1.append(timer)
        print("fib2(", number, ") -> ", value, " = ", timer, " seconds", sep="")

    ############################################ PART 2 ###########################################
    print("\nIterative algorithm for part 2")
    for number in n_2:
        value = fib2(number)
        timer = timeit.timeit(
            "fib2(" + str(number) + ")", "from __main__ import fib2", number=1
        )
        fib2_time_part2.append(timer)
        print("fib2(", number, ")", "=", timer, "seconds")

    plt.plot(n, fib1_time_part1, "r")
    # plt.plot(n, fib2_time_part1, "b")
    # plt.plot(n_2, fib2_time_part2, "g")
    plt.xlabel("n")
    plt.xlabel("time")
    plt.show()


if __name__ == "__main__":
    main()

