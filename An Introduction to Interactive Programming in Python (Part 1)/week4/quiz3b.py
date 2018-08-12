def f(x):
    if x % 2 == 0:
        x = x / 2
    elif x % 2 != 0:
        x = x * 3 + 1

    print(x)

    if x > 1:
        f(x)


def f1(n):
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        print(n)
