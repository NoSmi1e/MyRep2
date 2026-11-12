def matrix(n=1, m=None, value=0):
    if m is None:
        m = n

    result = []
    for _ in range(n):
        row = [value] * m
        result.append(row)

    return result
