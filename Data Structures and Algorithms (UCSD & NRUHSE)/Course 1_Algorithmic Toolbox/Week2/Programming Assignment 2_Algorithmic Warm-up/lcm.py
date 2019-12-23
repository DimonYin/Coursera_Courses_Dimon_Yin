# Uses python3

def gcd_fast(a, b):
    A = a
    B = b
    while B > 0:
        R = A % B
        A = B
        B = R
    return A

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm_fast(a, b):
    gcd = gcd_fast(a, b)
    return int(a*b/gcd)


numbers = input()
a, b = map(int, numbers.split())
print(lcm_fast(a, b))

