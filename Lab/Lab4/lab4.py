import numpy as np


def selection(arr, k):
    sl = []
    sv = []
    sr = []
    item = np.random.randint(0, len(arr))
    v = arr[item]
    for i in range(0, len(arr)):
        if arr[i] < v:
            sl.append(arr[i])
        elif arr[i] == v:
            sv.append(arr[i])
        elif arr[i] > v:
            sr.append(arr[i])

    if k <= len(sl):
        selection(sl, k)
    elif len(sl) < k and k <= (len(sl) + len(sv)):
        print("\nThe k value is:", k, " and selected: ", v)
    elif k > (len(sl) + len(sv)):
        selection(sr, k - len(sl) - len(sv))


if __name__ == "__main__":
    n = int(input("Enter the value n: "))
    k = int(input("Enter the value k: "))
    arr = []
    for i in range(0, n):
        arr.append(np.random.randint(0, n))

    selection(arr, k)
    print("The array is:", arr)
    print("Sort array is:", sorted(arr))

    print("\nDocument example: ")
    items = [5, 8, 9, 5, 0, 0, 1, 7, 6, 9]
    selection(items, 3)
    print("The array is:", items)
    print("Sort array is:", sorted(items))

