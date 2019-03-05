def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements
    of lst to lst.
    """
    for x in range (0,24):
        sum = lst[-1] + lst[-2] + lst[-3]
        lst.append(sum)
