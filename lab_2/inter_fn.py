import matplotlib.pyplot as plt
import numpy as np

from inter import inter_points_arrays

# INTER_NUM = int(input("Enter number of nodes:\n"))
NUM = 100


def in_fn(p):
    return 1 / (1 + p ** 2)


for INTER_NUM in range(5, NUM, 5):
    inp = np.linspace(-5, 5, NUM)
    out = in_fn(inp)

    arr_full = []
    arr = []

    for i in range(len(inp)):
        point = {"x": inp[i], "y": out[i]}
        arr_full.append(point)

        if i % round(NUM / INTER_NUM, 0) == 0:
            arr.append(point)

    plt.plot(inp, out)

    result = inter_points_arrays(arr_full, arr, NUM)

    err = 0

    for i in range(len(result)):
        err = err + (result[i] - arr_full[i]["y"]) ** 2

    print(f"Error for {INTER_NUM} nodes: {err / len(arr_full)}")
