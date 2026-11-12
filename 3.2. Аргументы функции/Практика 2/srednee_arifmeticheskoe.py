def mean(*args):
    total = 0
    count = 0

    for item in args:
        if type(item) == int or type(item) == float:
            total += item
            count += 1

    if count == 0:
        return 0
    return total / count
