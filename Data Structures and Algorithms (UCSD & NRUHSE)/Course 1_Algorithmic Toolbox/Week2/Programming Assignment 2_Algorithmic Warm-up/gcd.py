# Uses python3

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_fast(a, b):
    A = a
    B = b
    while B > 0:
        R = A % B
        A = B
        B = R
    return A


numbers = input()
a, b = map(int, numbers.split())
print(gcd_fast(a, b))
