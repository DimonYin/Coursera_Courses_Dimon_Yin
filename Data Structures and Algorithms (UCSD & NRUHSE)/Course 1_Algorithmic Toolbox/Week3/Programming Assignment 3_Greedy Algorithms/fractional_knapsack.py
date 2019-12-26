# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    maximal_value = 0.

    # print(capacity)
    # print(weights)
    # print(values)

    item = {}
    value_per_unit = []
    for num in range(len(weights)):
        vpu = float(values[num]/weights[num])
        value_per_unit.append(vpu)
        item[vpu] = weights[num]
    value_per_unit = sorted(value_per_unit, reverse=True)

    for index in range(len(value_per_unit)):
        if item[value_per_unit[index]] <= capacity:
            maximal_value = maximal_value + value_per_unit[index] * item[value_per_unit[index]]
            capacity = capacity - item[value_per_unit[index]]
        else:
            maximal_value = maximal_value + value_per_unit[index] * capacity
            capacity = 0

        if capacity == 0:
            return maximal_value

    return maximal_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
