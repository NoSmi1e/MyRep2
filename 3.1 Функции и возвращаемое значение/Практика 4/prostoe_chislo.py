def is_prime(num):
    if num == 1:
        return False

    for divisor in range(2, num):
        if num % divisor == 0:
            return False

    return True
