"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

def compute_primes(bound):

    """
    Return a list of the prime numbers in range(2, bound)
    """
    list1 = list()
    list2 = list()

    for i in range(2, bound):
        for j in range(1, i + 2):
            if i % j == 0:
                list1.append(j)
        if len(list1) == 2:
           # print(i)
            list2.append(i)
        list1 = []
    return list2
print(len(compute_primes(200)))
print(len(compute_primes(2000)))