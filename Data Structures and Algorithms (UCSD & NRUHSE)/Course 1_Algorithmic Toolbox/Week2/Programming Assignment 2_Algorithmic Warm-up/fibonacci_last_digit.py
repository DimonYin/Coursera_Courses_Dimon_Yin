# Uses python3
import sys


def calc_fib(n):
    # Create an array list of index
    FibList = [x for x in range(n + 1)]

    # Get the length
    length = len(FibList)

    if length == 1:
        return 0
    elif length == 2:
        return 1
    else:
        FibList[0] = 0
        FibList[1] = 1

        # Map the value from third index
        for m in range(2, len(FibList)):
            FibList[m] = (FibList[m - 1] + FibList[m - 2]) % 10

        return FibList[-1]  # Return the last number


n = int(input())
print(calc_fib(n))
