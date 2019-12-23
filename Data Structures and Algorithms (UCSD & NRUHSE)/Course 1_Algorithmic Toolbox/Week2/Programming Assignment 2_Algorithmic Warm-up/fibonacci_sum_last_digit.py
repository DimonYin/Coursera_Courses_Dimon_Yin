# Uses python3


# Get fibonacci number
def get_fibonacci(n):
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
            FibList[m] = FibList[m - 1] + FibList[m - 2]

        return FibList[-1]  # Return the last number


def get_fibonacci_huge_fast(n, m):
    if n <= 1:
        return n

    lis = [0, 1]
    period = -1
    for index in range(2, n + 1):
        lis.append(0)  # add a value being modified next
        lis[index] = (lis[index - 1] + lis[index - 2]) % m
        # Find period
        if lis[index] == 1 and lis[index - 1] == 0:
            period = index - 1
            break

    if period < 2:
        return get_fibonacci(n) % m
    else:
        return get_fibonacci(n % period) % m


def fibonacci_sum_fast(n):
    if n <= 1:
        return n

    sum = get_fibonacci_huge_fast(n + 2, 10)

    if sum == 0:
        return 9
    else:
        return sum - 1


n = int(input())
print(fibonacci_sum_fast(n))
