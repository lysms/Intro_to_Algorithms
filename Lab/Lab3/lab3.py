import random
import math


# Modular exponentiation
# Input: Two n-bit integers x and N, an integer exponent y
# output: (x**y) mod N
def modexp(x, y, N):
    if y == 0:
        return 1
    z = modexp(x, math.floor(y / 2), N)
    if y % 2 == 0:
        return (z ** 2) % N
    else:
        return x * (z ** 2) % N


# def primality3(N, K):
#     random_number = []
#     for i in range(0, K):
#         num = random.randint(1, N - 1)
#         random_number.append(num)
#     for i in random_number:
#         if modexp(i, N - 1, N) == 1:
#             return "yes"
#         else:
#             return "no"


# An algorithm for testing promality, with low error probability
# Input: Positive integer N, K
# Output: yes/no
def primality2(N, K):
    random_number = []
    result = True
    count = 0
    for i in range(0, K):
        num = random.randint(1, N - 1)
        random_number.append(num)

    for i in random_number:
        if modexp(i, N - 1, N) != 1:
            result = False
            count += 1
    print(N, "with Probaility prime: {:.2f}".format(1 - (count / K)))

    return result


if __name__ == "__main__":
    k = 25
    test = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
    ]
    com = [
        54915,
        70872,
        135039,
        174415,
        224338,
        288240,
        362258,
        405336,
        609274,
        642840,
        659557,
        764730,
        801361,
        822846,
        866756,
        886413,
        913964,
    ]
    c_num = [
        561,
        1105,
        1729,
        2465,
        2821,
        6601,
        8911,
        10585,
        15841,
        29341,
        41041,
        46657,
        52633,
        62745,
        63973,
        75361,
        101101,
        115921,
        126217,
        162401,
        172081,
        188461,
        252601,
        278545,
        294409,
        314821,
        334153,
        340561,
        399001,
        410041,
        449065,
        488881,
    ]
    print("\nmodexp function: ")
    print("3 ^  100 mod 5 is ", modexp(8, 86, 29))
    print("55 ^  10000 mod 45 is ", modexp(55, 10000, 45))
    print("3333 ^  4444 mod 5555 is ", modexp(3333, 444, 5555), "\n")

    print("Primality test:")
    for i in test:
        primality2(i, 25)

    print("\nComposite number:")
    for i in com:
        primality2(i, 25)

    print("\nCarmichael number:")
    for i in c_num:
        primality2(i, 25)

    # prob = []
    # for i in c_num:
    #     count = 0
    #     for j in range(0, 100):
    #         if primality3(i, k) == "yes":
    #             count += 1
    #     prob.append((count % 100) / k)

    # j = 0
    # for i in c_num:
    #     print("The car_number", i, "with probability prime:", prob[j])
    #     j += 1

