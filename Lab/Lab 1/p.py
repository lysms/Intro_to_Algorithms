import timeit
import time

n = [1, 5, 10, 15, 20, 25, 30, 35, 40, 41, 42, 43]


def fib1(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fib1(x - 1) + fib1(x - 2)


def main():
    start = time.time()
    for number in n:
        value = fib1(number)
        end = time.time()
        print("fib1(", number, ") -> ", value, " = ", end - start, " seconds", sep="")


if __name__ == "__main__":
    main()
