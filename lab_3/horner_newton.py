import matplotlib.pyplot as plt

def horner(factors, points):
    results = []

    for point in points:
        result = 0

        for i in reversed(range(1, len(factors))):
            result = (result + factors[i]) * point

        result += factors[0]

        results.append(result)

    return results


def newton_horner(factors, points):
    ress = []
    rev = loadedPointsStep

    for point in points:
        result = 0

        for i in reversed(range(1, len(factors))):
            result = (result + factors[i]) * (point - rev[i - 1])

        result += factors[0]
        ress.append(result)

    return ress


with open('interpolacja_H_gr_1.txt', 'r') as f:
    loadedFactors = f.readline().strip().split("\t")
    loadedPoints = list(map(lambda item: float(item.strip()), f.readline().strip().split("\t")))

    while '' in loadedFactors:
        loadedFactors.remove('')

    loadedFactors = list(map(lambda item: float(item.split("=")[1]), loadedFactors))


loadedPointsStep = loadedPoints[::10]
loadedPointsStep.append(loadedPoints[-1])

results = [horner(loadedFactors, loadedPointsStep)]

for i in range(0, len(loadedPointsStep)):
    results.append([])

    if i != 0:
        tmp = results[i - 1]
        for j in range(0, len(tmp) - 1):
            results[i].append((tmp[j + 1] - tmp[j]) / (loadedPointsStep[j + i] - loadedPointsStep[j]))

factors = []

for i in range(0, len(results)):
    if len(results[i]) == 0:
        continue

    factors.append(results[i][0])


res = newton_horner(factors, loadedPoints)
values = horner(loadedFactors, loadedPoints)

plt.plot(loadedPoints, values)
plt.plot(loadedPoints, res)
plt.grid()
plt.show()

error = 0

for i in range(len(res)):
    error += (values[i] - res[i]) ** 2

error /= len(res)

print(f"Error: {error}")
