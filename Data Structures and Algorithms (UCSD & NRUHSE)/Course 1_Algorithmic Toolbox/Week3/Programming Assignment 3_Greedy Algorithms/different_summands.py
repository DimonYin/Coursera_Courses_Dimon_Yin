# Uses python3
import sys

def optimal_summands(n):
    target = 0
    summands = []
    #write your code here
    for num in range(n):
        add = num + 1
        target = target + add
        summands.append(add)
        if target > n:
            target = target - add - add + 1
            summands.pop(-1)
            summands.pop(-1)
            summands.append(n - target)
            return summands
        elif target == n:
            return summands

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
