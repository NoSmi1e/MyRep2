def find_all(target, symbol):
    indexes = []
    for index in range(len(target)):
        if target[index] == symbol:
            indexes.append(index)
    return indexes
