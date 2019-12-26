# Uses python3
import sys
from operator import attrgetter
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    segments = sorted(segments, key=attrgetter('end'), reverse=True)
    points = []

    #write your code here
    while len(segments) > 0:
        segement = segments.pop()
        point = segement.end
        while len(segments) > 0 and point >= segments[-1].start:
            segments.pop()
        if point not in points:
            points.append(point)

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    #input = input()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
