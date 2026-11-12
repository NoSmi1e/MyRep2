def is_password_good(password):
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True

    if len(password) >= 8 and has_upper and has_lower and has_digit:
        return True
    else:
        return False
