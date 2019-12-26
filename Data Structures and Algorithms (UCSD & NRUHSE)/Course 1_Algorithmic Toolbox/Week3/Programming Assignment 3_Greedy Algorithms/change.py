# Uses python3


def get_change(rem):
    value_list = [1, 5, 10]
    # Sort first
    sorted_value_list = sorted(value_list, reverse=True)
    coin_list = []

    for value in sorted_value_list:
        coins = int(rem/value)
        coin_list = coin_list + [value] * coins  # Add needed coins into output coin list

        rem = rem - coins * value  # Update the remaining change

        # Once rem = 0, we just return the list
        if rem == 0:
            return len(coin_list)
    # If comes this step, that means there is no solution
    return "No solution"


m = int(input())
print(get_change(m))
