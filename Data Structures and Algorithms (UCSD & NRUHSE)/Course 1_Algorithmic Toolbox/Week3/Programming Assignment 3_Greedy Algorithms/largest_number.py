#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    controller = 0
    length = len(a)
    while controller < length:
        bm = "0"
        bm_index = -1
        for index in range(len(a)):
            temp1 = int(a[index] + bm)
            temp2 = int(bm + a[index])
            if temp1 > temp2:
                bm = a[index]
                bm_index = index

        a.pop(bm_index)  # Delete that added number
        res = res + bm
        controller += 1

    res = int(res)

    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    #input = input()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

