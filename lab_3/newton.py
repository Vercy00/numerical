import matplotlib.pyplot as plt

def newton_horner(factors, points):
    results = []
    rev = loadedXStep

    for point in points:
        result = 0

        for i in reversed(range(1, len(factors))):
            result = (result + factors[i]) * (point - rev[i - 1])

        result += factors[0]
        results.append(result)

    return results


with open('interpolacja_N_gr_1.txt', 'r') as f:
    loadedX = f.readline().strip().split("\t")
    loadedY = list(map(lambda item: float(item.strip()), f.readline().strip().split("\t")))

    while '' in loadedX:
        loadedX.remove('')

    loadedX = list(map(lambda item: float(item), loadedX))

    step = 10

    loadedXStep = loadedX[::step]
    loadedYStep = loadedY[::step]

results = [loadedYStep]

for i in range(0, len(loadedXStep)):
    results.append([])

    if i != 0:
        tmp = results[i - 1]
        for j in range(0, len(tmp) - 1):
            results[i].append((tmp[j + 1] - tmp[j]) / (loadedXStep[j + i] - loadedXStep[j]))

factors = []

for i in range(0, len(results)):
    if len(results[i]) == 0:
        continue

    factors.append(results[i][0])

res = newton_horner(factors, loadedX)

plt.plot(loadedX, loadedY)
plt.plot(loadedX, res)
plt.grid()
plt.show()

error = 0

for i in range(len(res)):
    error += (loadedY[i] - res[i]) ** 2

error /= len(res)

print(f"Error: {error}")

num = float(input("Enter x:\n"))
print(f"Result: {newton_horner(factors, [num])[0]}")