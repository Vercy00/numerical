import matplotlib.pyplot as plt

from inter import inter_points, inter_points_arrays

arr_full = []
arr = []

with open("./interpolacja_gr_1 1.txt", "r") as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.strip().split("\t"), lines))

    for i in range(0, len(lines[0])):
        point = {"x": float(lines[0][i]), "y": float(lines[1][i])}
        arr_full.append(point)

        if i % 5 == 0:
            arr.append({"x": float(lines[0][i]), "y": float(lines[1][i])})

for item in arr_full:
    plt.scatter(item["x"], item["y"])

result = inter_points_arrays(arr_full, arr, 52)

err = 0

for i in range(len(arr_full)):
    err = err + (result[i] - arr_full[i]["y"]) ** 2

print(f"Error: {err / len(arr_full)}")

INPUT_POINT = float(input("Enter point:\n"))

print(f"Result: {inter_points(arr, 1, [INPUT_POINT])[0]}")
