def is_prime(num):
    if num == 1:
        return False

    for divisor in range(2, num):
        if num % divisor == 0:
            return False

    return True


def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num
