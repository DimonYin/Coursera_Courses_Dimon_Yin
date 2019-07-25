def square(x):
    return x*x

import test

test.testEqual(square(3), 9)

def update_counts(letters, counts_d):
    for c in letters:
        counts_d[c] = 1
        if c in counts_d:
            counts_d[c] = counts_d[c] + 1

import test

counts = {'a': 3, 'b': 2}
update_counts("aaab", counts)
# 3 more occurrences of a, so 6 in all
test.testEqual(counts['a'], 6)
# 1 more occurrence of b, so 3 in all
test.testEqual(counts['b'], 3)

import test

test.testEqual(sorted([1, 7, 4]), [1, 4, 7])
test.testEqual(sorted([1, 7, 4], reverse=True), [7, 4, 1])