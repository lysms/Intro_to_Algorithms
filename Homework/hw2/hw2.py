import timeit
import matplotlib.pyplot as plt


def sum(n):
    fact = 0
    for i in range(1, n + 1):
        fact = fact * i
    return fact


if __name__ == "__main__":
    time = []
    n = 1000
    slot = []
    for i in range(0, n):
        slot.append(i * 2)
    for i in range(0, n):
        timer = timeit.timeit(
            "sum(" + str(i) + ")", "from __main__ import sum", number=1
        )
        time.append(timer)

    for i in range(0, n):
        print(time[i])
    plt.plot(slot, time, "r")
    plt.ylabel("n")
    plt.xlabel("time")

    plt.show()
