# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.append(0)
    stops.append(distance)
    stops = sorted(stops)

    fulltank = tank

    numRefills = 0
    for stop in range(len(stops)-1):
        n_d = stops[stop + 1] - stops[stop]
        if n_d > fulltank:
            return -1

        if stop == 0:
            p_d = stops[stop]
        else:
            p_d = stops[stop] - stops[stop-1]

        tank = tank - p_d
        if tank < n_d:
            tank = fulltank
            numRefills += 1

    return numRefills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
