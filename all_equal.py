def all_equal(list):
    allEqual = True

    for result in list:
        isEqual = result == list[0]
        if not isEqual:
            allEqual = False

    return allEqual
