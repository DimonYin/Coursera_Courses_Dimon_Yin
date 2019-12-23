# python3


def find_max_pairwise_product(number, numbers):
    max1 = 0  # Max number in the list
    max2 = 0  # Second max number in the list
    max_index_1 = -1  # the index of the max number

    # Find the max number and record its index
    for n in range(number):
        if numbers[n] > max1:
            max1 = numbers[n]
            max_index_1 = n

    # Find the second max number
    for n in range(number):
        if numbers[n] > max2 and n != max_index_1:
            max2 = numbers[n]

    return max1 * max2  # Return the product


if __name__ == '__main__':
    input_n = int(input())
    input_list = [int(x) for x in input().split()]
    print(find_max_pairwise_product(input_n, input_list))
