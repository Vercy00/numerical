import matplotlib.pyplot as plt
import numpy as np


def inter_fn(arr, obj, x):
    tmp_1 = 1
    tmp_2 = 1

    for tmp_item in arr:
        if tmp_item["x"] == obj["x"] and tmp_item["y"] == obj["y"]:
            continue

        tmp_1 = tmp_1 * (x - tmp_item["x"])
        tmp_2 = tmp_2 * (obj["x"] - tmp_item["x"])

    return tmp_1 / tmp_2


def inter_points(arr, num=100, points=np.array([])):
    mm = min(arr, key=lambda t: t["x"])["x"]
    mx = max(arr, key=lambda t: t["x"])["x"]

    x = np.array(points) if len(points) != 0 else np.linspace(mm, mx, num)
    fn = 0

    for item in arr:
        fn = fn + (item["y"] * inter_fn(arr, item, x))
        plt.scatter(item["x"], item["y"])

    if len(x) > 1:
        plt.plot(x, fn)
        plt.grid()
        plt.show()

    return fn


def inter_points_arrays(arr_full, arr=np.array([]), num=100, points=np.array([])):
    if len(arr) == 0:
        arr = arr_full

    mm = min(arr_full, key=lambda t: t["x"])["x"]
    mx = max(arr_full, key=lambda t: t["x"])["x"]

    x = np.array(points) if len(points) != 0 else np.linspace(mm, mx, num)
    fn = 0

    for item in arr:
        fn = fn + (item["y"] * inter_fn(arr, item, x))
        plt.scatter(item["x"], item["y"])

    if len(x) > 1:
        plt.plot(x, fn)
        plt.grid()
        plt.show()

    return fn
