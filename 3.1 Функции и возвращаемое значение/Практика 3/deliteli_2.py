def get_factors(num):
    factors = []
    for number in range(1, num + 1):
        if num % number == 0:
            factors.append(number)
    return factors


def number_of_factors(num):
    factors = get_factors(num)
    return len(factors)
