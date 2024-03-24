import time

def horner_1(factors, points):
    start = time.time()
    results = []

    for point in points:
        result = 0

        for i in range(len(factors)):
            result += factors[i] * point ** i

        results.append(result)

    print(f'{time.time() - start}ms')
    return results


def horner_2(factors, points):
    start = time.time()
    results = []

    for point in points:
        result = 0

        for i in reversed(range(1, len(factors))):
            result = (result + factors[i]) * point

        result += factors[0]

        results.append(result)

    print(f'{time.time() - start}ms')
    return results


if __name__ == '__main__':
    with open('interpolacja_H_gr_1.txt', 'r') as f:
        loadedFactors = f.readline().strip().split("\t")
        loadedPoints = list(map(lambda item: float(item.strip()), f.readline().strip().split("\t")))

        while '' in loadedFactors:
            loadedFactors.remove('')

        loadedFactors = list(map(lambda item: float(item.split("=")[1]), loadedFactors))

    for i in range(1, len(loadedFactors)):
        factors = loadedFactors[0:i]

        print(f'\n{factors}')

        horner_1(factors, loadedPoints)
        print(loadedPoints[:1], horner_2(factors, loadedPoints[:1]))
